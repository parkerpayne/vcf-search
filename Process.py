from FindDatatypes import findHeaderLine

def process(file, parameters, columnIndex, columnType):
    header = findHeaderLine(file)
    delim = '\t'
    if file.endswith('.csv'):
        delim = ','
    with open(f'temp', 'w') as opened:
        opened.write(header)
        foundHeader = False
        for row in open(file, 'r'):
            if row == header:
                foundHeader = True
                continue
            if foundHeader == False:
                continue
            line = row.strip().split(delim)
            valid = True
            for param in parameters:
                col = param[0]
                operator = param[1]
                bar = param[2]
                nas = param[3]

                value = line[columnIndex[col]]
                if value in ['-', '.']:
                    value = ''
                
                if value == '' and nas:
                    continue
                match operator:
                    case '==':
                        if columnType[col](value) != columnType[col](bar):
                            valid = False
                    case '>=':
                        if columnType[col](value) < columnType[col](bar):
                            valid = False
                    case '<=':
                        if columnType[col](value) > columnType[col](bar):
                            valid = False
                    case '>':
                        if columnType[col](value) <= columnType[col](bar):
                            valid = False
                    case '<':
                        if columnType[col](value) >= columnType[col](bar):
                            valid = False
                    case '!=':
                        if columnType[col](value) == columnType[col](bar):
                            valid = False
                    case 'Contains':
                        if str(bar) not in str(value):
                            valid = False
            if valid:
                opened.write(row)