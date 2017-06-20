# tutorial: https://openpyxl.readthedocs.io/en/default/tutorial.html#accessing-many-cells

import openpyxl

# read excel
wb = openpyxl.load_workbook(my_excel)  # read excel file
my_sheet = wb.get_sheet_by_name(sheet_name) # read sheet
col = my_sheet['A4':'A10']  # read multiple rows in a col, here 'A', 'B'.. indicates cols in Excel
for elem in col:
    print elem.value # access to the cell value
