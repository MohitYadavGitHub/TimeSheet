import openpyxl
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
from pprint import pprint as pp
import pandas as pd

# ## Open the Excel 
# wb = openpyxl.load_workbook('template.xlsx')
# pp(dir(wb))
# 
# ## find sheets in excel
# allSheets  = wb.get_sheet_names()
# pp (allSheets)
# 
# ## Get List of Employees
# empSh = wb.get_sheet_by_name ('Employees')
# print (empSh['A2'].value)

## pandas stuff

# df = pd.read_excel("template.xlsx")
# xlsx = pd.ExcelFile('template.xls')
with pd.ExcelFile('template.xlsx') as xls:
     df1 = pd.read_excel(xls, 'SourceInfo')
     df2 = pd.read_excel(xls, 'Employees')
     df3 = pd.read_excel(xls, 'CurrentMonth')
     
     print(df1)
     print(df2)
     print(df3)
     