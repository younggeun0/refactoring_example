const invoices = require("./invoices.json");
const plays = require("./plays.json");
const { createStatementData } = require("./createStatementData.js");

// 리팩터링한 계산 함수들을 사용하여 HTML 결과를 출력하는 기능을 추가하고 싶음
// 이를 위해 단개 쪼개기를 사용
// 1. 필요한 데이터를 처리(계산 단계)
// 2. 결과를 텍스트나 HTML로 표현(포맷팅 단계)

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

    function usd(aNumber) {
        return new Intl.NumberFormat("en-US", {
            style: "currency", currency: "USD",
            minimumFractionDigits: 2
        }).format(aNumber/100);
    }
}

// main
invoices.forEach(invoice => {
    const result = statement(invoice, plays);
    console.log(result);
});