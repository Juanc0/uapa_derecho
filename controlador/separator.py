import xlrd
book = xlrd.open_workbook('../info.xlsx')
sheet = book.sheet_by_index(0)

data = set()

with open('dnis.txt', 'w+') as file:
    for i in range(1, sheet.nrows):
        dni = str(sheet.cell_value(i, 0)).split('.')[0]
        if not dni in data:
            file.write(dni + '\n')
            data.add(dni)
