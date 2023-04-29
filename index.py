import json
import unittest

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
    total_amount = 0
    volume_credits = 0
    result = f"청구 내역 (고객명: {invoice['customer']})\n"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        this_amount = 0

        if play['type'] == 'tragedy':
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == 'comedy':
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)
            this_amount += 300 * perf['audience']
        else:
            raise Exception(f"알 수 없는 장르: {play['type']}")

        # 포인트를 적립한다.
        volume_credits += max(perf['audience'] - 30, 0)

        # 희극 관객 5명마다 추가 포인트를 제공한다.
        if 'comedy' == play['type']:
            volume_credits += perf['audience'] // 5

        # 청구 내역을 출력한다.
        result += f"  {play['name']}: ${this_amount/100:.2f} ({perf['audience']} 석)\n"
        total_amount += this_amount

    result += f"총액: ${total_amount/100:.2f}\n"
    result += f"적립 포인트: {volume_credits}\n"
    return result


if __name__ == "__main__":
    unittest.main()

