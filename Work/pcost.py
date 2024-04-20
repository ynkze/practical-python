import sys
import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Error. Usage: {sys.argv[0]} portfolio_file')
    
    cost = portfolio_cost(sys.argv[1])
    print("Total cost: ", cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)