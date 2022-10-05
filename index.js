const invoices = require("./invoices.json");
const plays = require("./plays.json");
const { createStatementData } = require("./createStatementData.js");

function statement(invoice, plays) {
    return renderPlainText(createStatementData(invoice, plays));
}

function renderPlainText(data) {
    let result = `청구 내역 (고객명: ${data.customer})\n`;

    for (let perf of data.performances) {
        result += ` ${perf.play.name}: ${usd(perf.amount)} (${perf.audience}석)\n`;
    }

    result += `총액: ${usd(data.totalAmount)}\n`;
    result += `적립 포인트: ${data.totalVolumeCredits}\n`;
    return result;
}

// 단계 쪼개기로 데이터 처리를 모듈화한 덕분에 계산 코드를 중복하지 않고도 HTML 버전을 만들 수 있었음
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
        style: "currency", currency: "USD",
        minimumFractionDigits: 2
    }).format(aNumber/100);
}

// main
invoices.forEach(invoice => {
    const result = statement(invoice, plays);
    console.log(result);

    const result2 = htmlStatement(invoice, plays);
    console.log(result2);
});