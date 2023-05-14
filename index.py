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

def statement(invoice, plays):
    return render_plain_text(create_statement_data(invoice, plays))

def render_plain_text(data):


    result = f"청구 내역 (고객명: {data['customer']})\n"

    for perf in data['performances']:
        # 청구 내역을 출력한다.
        result += f"  {perf['play']['name']}: ${perf['amount']/100:.2f} ({perf['audience']} 석)\n"


    result += f"총액: ${data['total_amount']/100:.2f}\n"
    result += f"적립 포인트: {data['total_volume_credit']}\n"
    return result


if __name__ == "__main__":
    unittest.main()

