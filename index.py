import json
import unittest
from create_statement_data import create_statement_data

invoices = None
plays = None

with open('./invoices.json') as f:
    invoices = json.load(f)

with open('./plays.json') as f:
    plays = json.load(f)

class TestStatement(unittest.TestCase):
    def test_statement(self):
        print(statement(invoices[0], plays))
        self.assertEqual(statement(invoices[0], plays),"""청구 내역 (고객명: BigCo)
  Hamlet: $650.00 (55 석)
  As You Like it: $580.00 (35 석)
  Othello: $500.00 (40 석)
총액: $1730.00
적립 포인트: 47
""")

    def test_html_statement(self):
        print(html_statement(invoices[0], plays))
        self.assertEqual(html_statement(invoices[0], plays),"""<h1>청구 내역 (고객명: BigCo)</h1>
<table>
<tr><th>연극</th><th>좌석 수</th><th>금액</th></tr><tr><td>Hamlet</td><td>($650.00)</td><td>55 석</td></tr>
<tr><td>As You Like it</td><td>($580.00)</td><td>35 석</td></tr>
<tr><td>Othello</td><td>($500.00)</td><td>40 석</td></tr>
</table>
<p>총액: <em>$1730.00</em></p>
<p>적립 포인트: <em>47</em>점</p>
""")

def statement(invoice, plays):
    return render_plain_text(create_statement_data(invoice, plays))

def html_statement(invoice, plays):
    return render_html(create_statement_data(invoice, plays))

def render_plain_text(data):
    result = f"청구 내역 (고객명: {data['customer']})\n"

    for perf in data['performances']:
        # 청구 내역을 출력한다.
        result += f"  {perf['play']['name']}: ${perf['amount']/100:.2f} ({perf['audience']} 석)\n"


    result += f"총액: ${data['total_amount']/100:.2f}\n"
    result += f"적립 포인트: {data['total_volume_credit']}\n"
    return result

def render_html(data):
    result = f"<h1>청구 내역 (고객명: {data['customer']})</h1>\n"
    result += "<table>\n"
    result += "<tr><th>연극</th><th>좌석 수</th><th>금액</th></tr>"
    for perf in data['performances']:
        result += f"<tr><td>{perf['play']['name']}</td><td>(${perf['amount']/100:.2f})</td><td>{perf['audience']} 석</td></tr>\n"
    result += "</table>\n"
    result += f"<p>총액: <em>${data['total_amount']/100:.2f}</em></p>\n"
    result += f"<p>적립 포인트: <em>{data['total_volume_credit']}</em>점</p>\n"
    return result

if __name__ == "__main__":
    unittest.main()

