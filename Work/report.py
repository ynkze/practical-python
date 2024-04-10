from fileparse import parse_csv

def read_portfolio(filename):
    with open(filename) as lines:
        return parse_csv(lines, types=[str, int, float])

def read_prices(filename):
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))


def print_report(portfolio, prices):
    report = []
    portfolio_cost = 0.0
    current_value = 0.0
    
    print(f'{"Name":>10s} {"Quantity":>10s} {"Price":>10s} {"Change":>10s}')
    print('---------- ---------- ---------- -----------')
    
    for stock in portfolio:
        stock_change = prices[stock['name']] - stock['price']
        report.append((stock['name'], stock['shares'], stock['price'], stock_change))
        print(f"{stock['name']:>10s} {stock['shares']:>10d} {stock['price']:>10.2f} {stock_change:>10.2f}")

        portfolio_cost += stock["shares"] * stock["price"]
        if stock["name"] in prices:
            current_value += stock["shares"] * prices[stock["name"]]


    print(f'\nPortfolio cost: {portfolio_cost:.2f}')
    print(f'Current value: {current_value:.2f}')
    print(f'Total gain/loss: {current_value - portfolio_cost:.2f}')

def portfolio_report(portfolio_file, price_file):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(price_file)

    print_report(portfolio, prices)

def main(argv):
    if len(argv) < 3:
        raise SystemExit(f'Error. Usage: {sys.argv[0]} portfolio_file price_file')

    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)