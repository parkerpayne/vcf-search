def findHeaderLine(file):
    oldline = ''
    first = True
    for line in open(file):
        if first:
            oldline = line
            first = False
        if line.startswith('#'):
            oldline = line
        else:
            return oldline

def find_datatypes(file, parameters):
    bloat = findHeaderLine(file)
    columnIndex = {}
    columnType = {}
    for param in parameters:
        columnType[param[0]] = int
    delim = '\t'
    first = True
    if file.endswith('.csv'):
        delim = ','
    for row in open(file, 'r'):
        line = row.strip().split(delim)
        if first:
            if not bloat == row:
                continue
            first = False
            header = row
            for index, col in enumerate(line):
                if col in columnType:
                    columnIndex[col] = index
            continue
        if row == header: continue
        for col in columnIndex:
            value = line[columnIndex[col]]
            if value in ['-', '.']:
                value = ''
            if value == '':
                continue
            if columnType[col] == int:
                try:
                    int(value)
                    if '.' in value:
                        columnType[col] = float
                except:
                    try:
                        float(value)
                        columnType[col] = float
                    except:
                        columnType[col] = str
    return columnIndex, columnType