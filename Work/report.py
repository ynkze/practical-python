from fileparse import parse_csv
from stock import Stock
from tableformat import create_formatter

def read_portfolio(filename):
    with open(filename) as lines:
        portdicts = parse_csv(lines, types=[str, int, float])
        return [Stock(d['name'], d['shares'], d['price']) for d in portdicts]

def read_prices(filename):
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    report = []
    
    for stock in portfolio:
        current_price = prices[stock.name]
        stock_change = current_price - stock.price
        report.append((stock.name, stock.shares, current_price, stock_change))
    
    return report

def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (names, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_file, price_file, fmt='txt'):
    # Read data files
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(price_file)

    # Create report data
    report = make_report(portfolio, prices)
    
    # Print it out
    formatter = create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) != 4:
        raise SystemExit(f'Error. Usage: {sys.argv[0]} portfolio_file price_file format_type')

    portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)