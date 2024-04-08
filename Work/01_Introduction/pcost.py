# Exercise 1.27/1.33
import sys
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                total_cost += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    print(f'Total cost {total_cost:.2f}')

filename = 'Work/Data/portfolio.csv'
if len(sys.argv) >= 2:
    filename = sys.argv[1]

portfolio_cost(filename)
