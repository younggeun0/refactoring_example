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
    def play_for(perf):
        return plays[perf['playID']]
    
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

    def volume_credits_for(perf):
        result = max(perf['audience'] - 30, 0)

        # 희극 관객 5명마다 추가 포인트를 제공한다.
        if 'comedy' == play_for(perf)['type']:
            result += perf['audience'] // 5

        return result

    def enrich_performance(a_performance):
        result = a_performance.copy()
        result['play'] = play_for(result)
        result['amount'] = amount_for(result)
        result['volume_credits'] = volume_credits_for(result)
        return result

    statement_data = {}
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = list(map(enrich_performance, invoice['performances']))

    return render_plain_text(statement_data)

    
def render_plain_text(data):
    def total_volume_credit():
        return sum([perf['volume_credits'] for perf in data['performances']])
    
    def total_amount():
        return sum([perf['amount'] for perf in data['performances']])


    result = f"청구 내역 (고객명: {data['customer']})\n"

    for perf in data['performances']:
        # 청구 내역을 출력한다.
        result += f"  {perf['play']['name']}: ${perf['amount']/100:.2f} ({perf['audience']} 석)\n"


    result += f"총액: ${total_amount()/100:.2f}\n"
    result += f"적립 포인트: {total_volume_credit()}\n"
    return result



if __name__ == "__main__":
    unittest.main()

