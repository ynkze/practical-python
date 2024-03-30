# Exercise 1.27/1.33
import sys

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, encoding='utf-8') as f:
        next(f)
        for line in f:
            row = line.split(',')
            total_cost += int(row[1]) * float(row[2])

    print(f'Total cost {total_cost:.2f}')

filename = 'Work/Data/portfolio.csv'
if len(sys.argv) >= 2:
    filename = sys.argv[1]

portfolio_cost(filename)
