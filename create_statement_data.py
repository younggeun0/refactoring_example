class PerformanceCalculator:
    def __init__(self, a_performance, a_play):
        self.performance = a_performance
        self.play = a_play

    @property
    def amount(self):
        raise NotImplementedError

    @property
    def volume_credits(self ):
        return max(self.performance['audience'] - 30, 0)
    
class TragedyCalculator(PerformanceCalculator):
    @property
    def amount(self):
        result = 40000
        if self.performance['audience'] > 30:
            result += 1000 * (self.performance['audience'] - 30)
        
        return result
    
class ComedyCalculator(PerformanceCalculator):
    @property
    def amount(self):
        result = 30000
        if self.performance['audience'] > 20:
            result += 10000 + 500 * (self.performance['audience'] - 20)
        result += 300 * self.performance['audience']
    
        return result
    
    @property
    def volume_credits(self):
        return super().volume_credits + self.performance['audience'] // 5
    

def create_performance_calculator(a_performance, a_play):
    if a_play['type'] == 'tragedy':
        return TragedyCalculator(a_performance, a_play)
    elif a_play['type'] == 'comedy':
        return ComedyCalculator(a_performance, a_play)
    else:
        raise Exception(f"알 수 없는 장르: {a_play['type']}")

def create_statement_data(invoice, plays):
    def play_for(perf):
        return plays[perf['playID']]
    


    def enrich_performance(a_performance):
        calculator = create_performance_calculator(a_performance, play_for(a_performance))

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
    