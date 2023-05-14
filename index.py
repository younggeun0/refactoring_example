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
    def amount_for(perf):
        result = 0

        if play_for(perf)['type'] == 'tragedy':
            result = 40000
            if perf['audience'] > 30:
                result += 1000 * (perf['audience'] - 30)
        elif play_for(perf)['type'] == 'comedy':
            result = 30000
            if perf['audience'] > 20:
                result += 10000 + 500 * (perf['audience'] - 20)
            result += 300 * perf['audience']
        
        return result 

    def play_for(perf):
        return plays[perf['playID']]

    def volume_credits_for(perf):
        result = max(perf['audience'] - 30, 0)

        # 희극 관객 5명마다 추가 포인트를 제공한다.
        if 'comedy' == play_for(perf)['type']:
            result += perf['audience'] // 5

        return result
    
    def total_volume_credit():
        result = 0
        for perf in invoice['performances']:
            result += volume_credits_for(perf)
        return result
    
    def total_amount():
        result = 0
        for perf in invoice['performances']:
            result += amount_for(perf)
        return result


    result = f"청구 내역 (고객명: {invoice['customer']})\n"

    for perf in invoice['performances']:
        # 청구 내역을 출력한다.
        result += f"  {play_for(perf)['name']}: ${amount_for(perf)/100:.2f} ({perf['audience']} 석)\n"


    result += f"총액: ${total_amount()/100:.2f}\n"
    result += f"적립 포인트: {total_volume_credit()}\n"
    return result



if __name__ == "__main__":
    unittest.main()

