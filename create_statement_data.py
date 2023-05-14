def create_statement_data(invoice, plays):
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
    