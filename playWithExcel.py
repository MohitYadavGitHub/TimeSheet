import openpyxl
import datetime
import pandas
import pdb
import pprint


wb = openpyxl.load_workbook('template.xlsx')

sheetNames = wb.get_sheet_names()

empSheet = wb.get_sheet_by_name('Employees')
target = wb.copy_worksheet(empSheet)

print (empSheet['A2'].value)
print (dir(empSheet))

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dir(wb))
pp.pprint(dir(target))
print (target.sheet_state)
wb.save('template.xlsx')