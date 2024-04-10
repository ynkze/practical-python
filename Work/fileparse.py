import csv

def parse_csv(lines, select=[], types=[], has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

    # Error checking for selecting when there is no headers
    if select and not has_headers:
        raise RuntimeError("select argument requires headers")

    rows = csv.reader(lines, delimiter=delimiter)

    # Read headers
    headers = next(rows) if has_headers else []

    # Selected columns only
    if select:
        selected_index = [headers.index(colname) for colname in select]
        headers = select
    else:
        selected_index = []

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row: # skip if no data
            continue
        
        # Pick specific column
        if selected_index:
            row = [row[index] for index in selected_index]

        # Type conversion for row and error checking if unable to convert
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {rowno}: Couldn\'t convert {row}')
                    print(f'Row {rowno}: Reason {e}')
                continue

        # Headers formatting
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records
