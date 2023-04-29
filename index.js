const invoices = require("./invoices.json");
const plays = require("./plays.json");

function statement(invoice, plays) {
    let totalAmount = 0;
    let volumeCredits = 0;
    let result = `청구 내역 (고객명: ${invoice.customer})\n`;
    const format = new Intl.NumberFormat("en-US", {
        style: "currency", currency: "USD",
        minimumFractionDigits: 2
    }).format;

    for (let perf of invoice.performances) {
        const play = plays[perf.playID];
        let thisAmount = amountFor(perf, play);

        // 포인트를 적립한다.
        volumeCredits += Math.max(perf.audience - 30, 0);

        // 희극 관객 5명마다 추가 포인트를 제공한다.
        if ("comedy" === play.type) volumeCredits += Math.floor(perf.audience / 5);

        // 청구 내역을 출력한다.
        result += ` ${play.name}: ${format(thisAmount / 100)} (${perf.audience}석)\n`;
        totalAmount += thisAmount;
    }

    result += `총액: ${format(totalAmount / 100)}\n`;
    result += `적립 포인트: ${volumeCredits}\n`;
    return result;

    function amountFor(aPerformance, play) {
        let result = 0;

        switch (play.type) {
            case "tragedy": // 비극
                result = 40000;
                if (aPerformance.audience > 30) {
                    result += 1000 * (aPerformance.audience - 30);
                }
                break;
            case "comedy": // 희극
                result = 30000;
                if (aPerformance.audience > 20) {
                    result += 10000 + 500 * (aPerformance.audience - 20);
                }
                result += 300 * aPerformance.audience;
                break;
            default:
                throw new Error(`알 수 없는 장르 : ${play.type}`);
        }

        return result;
    }
}

invoices.forEach(invoice => {
    const input1 = statement(invoice, plays);
    const result =
        "청구 내역 (고객명: BigCo)\n Hamlet: $650.00 (55석)\n As You Like it: $580.00 (35석)\n Othello: $500.00 (40석)\n총액: $1,730.00\n적립 포인트: 47\n";
    console.assert(input1 === result, "[Assertion] input1 !== output1");

    console.log(result);
});