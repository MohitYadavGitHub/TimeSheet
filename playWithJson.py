import json
import datetime
import pdb

allDb = {}

tdy = datetime.date.today()
monthEntry = {}

employees = ['emp1', 'emp2', 'emp3']

rowData = [ 'MonthlySalary', 'Attendance', 'Advance Balance', 'Advance For Month', 'Salary For Month' ]
for emp in employees:
    for x in range(1, 13):
        month = str(x) + '_' + str (tdy.year)   
        print month
        monthEntry[month] = rowData        
    allDb[emp] = monthEntry
    
s = json.dumps(allDb,indent=4,sort_keys=True,separators=(',',':'))
print s


with open('database.db','w') as ff:
    ff.write(s)
