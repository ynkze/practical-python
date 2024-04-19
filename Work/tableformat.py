class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>'+ h + '</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print('<td>' + d + '</td>',end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format %s' % fmt)

def print_table(portfolio, col, formatter):
    formatter.headings(col)    
    for stock in portfolio:
        rowdata = []
        for colname in col:
            rowdata.append(str(getattr(stock, colname)))
        formatter.row(rowdata)
