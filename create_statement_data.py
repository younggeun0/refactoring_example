class PerformanceCalculator:
    def __init__(self, a_performance, a_play):
        self.performance = a_performance
        self.play = a_play

    # def amount(self):
    #     raise NotImplementedError

    # def volume_credits(self):
    #     return max(self.performance['audience'] - 30, 0)

    @property
    def amount(self):
        result = 0

        if self.play['type'] == 'tragedy':
            result = 40000
            if self.performance['audience'] > 30:
                result += 1000 * (self.performance['audience'] - 30)
        elif self.play['type'] == 'comedy':
            result = 30000
            if self.performance['audience'] > 20:
                result += 10000 + 500 * (self.performance['audience'] - 20)
            result += 300 * self.performance['audience']
        
        return result 

    @property
    def volume_credits(self ):
        result = max(self.performance['audience'] - 30, 0)

        # 희극 관객 5명마다 추가 포인트를 제공한다.
        if 'comedy' == self.play['type']:
            result += self.performance['audience'] // 5

        return result


def create_statement_data(invoice, plays):
    def play_for(perf):
        return plays[perf['playID']]
    


    def enrich_performance(a_performance):
        calculator = PerformanceCalculator(a_performance, play_for(a_performance))

        result = a_performance.copy()
        result['play'] = calculator.play
        result['amount'] = calculator.amount
        result['volume_credits'] = calculator.volume_credits
        return result
    
    def total_volume_credit(data):
        return sum([perf['volume_credits'] for perf in data['performances']])
    
    def total_amount(data):
        return sum([perf['amount'] for perf in data['performances']])

    statement_data = {}
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = list(map(enrich_performance, invoice['performances']))
    statement_data['total_amount'] = total_amount(statement_data)
    statement_data['total_volume_credit'] = total_volume_credit(statement_data)

    return statement_data
    