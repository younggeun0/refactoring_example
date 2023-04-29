const { createStatementData } = require("./createStatementData");
const invoices = require("./invoices.json");
const plays = require("./plays.json");

function statement(invoice, plays) {
    return renderPlainText(createStatementData(invoice, plays));
}

function htmlStatement(invoice, plays) {
    return renderHtml(createStatementData(invoice, plays));
}

function renderHtml(data) {
    let result = `<h1>청구내역 (고객명: ${data.customer})</h1>\n`;
    result += "<table>\n";
    result += "<tr><th>연극</th><th>좌석 수</th><th>금액</th></tr>";
    for (let perf of data.performances) {
        result += ` <tr><td>${perf.play.name}</td><td>(${perf.audience}석)</td>`;
        result += `<td>${usd(perf.amount)}</td></tr>\n`;
    }
    result += "</table>\n";
    result += `<p>총액: <em>${usd(data.totalAmount)}</em></p>\n`;
    result += `<p>적립 포인트: <em>${data.totalVolumeCredits}</em>점</p>\n`;
    return result;
}

function usd(aNumber) {
    return new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD",
        minimumFractionDigits: 2,
    }).format(aNumber / 100);
}

function renderPlainText(data) {
    let result = `청구 내역 (고객명: ${data.customer})\n`;
    for (let perf of data.performances) {
        // 청구 내역을 출력한다.
        result += ` ${perf.play.name}: ${usd(perf.amount)} (${perf.audience}석)\n`;
    }

    result += `총액: ${usd(data.totalAmount)}\n`;
    result += `적립 포인트: ${data.totalVolumeCredits}\n`;
    return result;
}

invoices.forEach((invoice) => {
    const input1 = statement(invoice, plays);
    const output1 =
        "청구 내역 (고객명: BigCo)\n Hamlet: $650.00 (55석)\n As You Like it: $580.00 (35석)\n Othello: $500.00 (40석)\n총액: $1,730.00\n적립 포인트: 47\n";
    console.assert(input1 === output1, "[Assertion] input1 !== output1");
    console.log(output1);

    const input2 = htmlStatement(invoice, plays);
    const output2 =
        "<h1>청구내역 (고객명: BigCo)</h1>\n<table>\n<tr><th>연극</th><th>좌석 수</th><th>금액</th></tr> <tr><td>Hamlet</td><td>(55석)</td><td>$650.00</td></tr>\n <tr><td>As You Like it</td><td>(35석)</td><td>$580.00</td></tr>\n <tr><td>Othello</td><td>(40석)</td><td>$500.00</td></tr>\n</table>\n<p>총액: <em>$1,730.00</em></p>\n<p>적립 포인트: <em>47</em>점</p>\n";
    console.assert(input2 === output2, "[Assertion] input2 !== output2");
    console.log(output2);
});
