from follow import follow
from tableformat import create_formatter
from report import read_portfolio
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dict(rows, keys):
    for row in rows:
        yield dict(zip(keys, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0,1,4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dict(rows, ['name', 'price', 'change'])
    return rows

# def filter_symbols(rows, names):
#     for row in rows:
#         if row['name'] in names:
#             yield row

def ticker(portfile, logfile, fmt):
    portfolio = read_portfolio(portfile)

    formatter = create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])

    # follow log file -> process data we want from logs into dict -> select ticker we have in portfolio
    logs = follow(logfile)
    logs = parse_stock_data(logs)
    logs = (log for log in logs if log['name'] in portfolio)

    for log in logs:
        formatter.row([log['name'], f"{log['price']:0.2f}", f"{log['change']:0.2f}"])

if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
