# Exercise 2.4

import csv

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if not row:
                continue
            prices[row[0]] = float(row[1])

    return prices

def read_portfolio(filename):
    portfolio = []
    with open(filename, encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'qty': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)

    return portfolio

def make_report(portfolio, prices):
    report = []
    print(f'{"Name":>10s} {"Quantity":>10s} {"Price":>10s} {"Change":>10s}')
    print('---------- ---------- ---------- -----------')
    for stock in portfolio:
        stock_change = prices[stock['name']] - stock['price']
        report.append((stock['name'], stock['qty'], stock['price'], stock_change))
        print(f"{stock['name']:>10s} {stock['qty']:>10d} {stock['price']:>10.2f} {stock_change:>10.2f}")

    return

prices = read_prices('Work/Data/prices.csv')
portfolio = read_portfolio('Work/Data/portfolio.csv')

make_report(portfolio, prices)

portfolio_cost = 0.0
current_value = 0.0
for stock in portfolio:
    portfolio_cost += stock["qty"] * stock["price"]
    if stock["name"] in prices:
        current_value += stock["qty"] * prices[stock["name"]]


print(f'\nPortfolio cost: {portfolio_cost:.2f}')
print(f'Current value: {current_value:.2f}')
print(f'Total gain/loss: {current_value - portfolio_cost:.2f}')
