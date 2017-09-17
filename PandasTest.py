import pandas as pd
import numpy as np
from pprint import pprint as pp
import datetime as baseDt
from datetime import datetime as dtime
from pprint import pprint as pp
from dIM import get_datetime_range


def flattenMixList(inputList):
     final = []
     for i in inputList:
         if type(i) == list or type(i)== np.ndarray:
             for j in i:
                 final.append(j)
         else:
             final.append(i)
     return(final)        


## start of function

currentDate = dtime.now()
currentMonth = currentDate.month
currentYear= currentDate.year
dObj,dMon = get_datetime_range(currentYear, currentMonth)
# print (dObj,dMon )

# Multi indexing
baseSeries = pd.Series(flattenMixList([0,0,np.zeros(len(dObj)),0,0]),
                       index = flattenMixList (['MonthlySalary',
                                 dObj,
                                 'Advance Balance',
                                 'Balance For Month',
                                 'Total Salary']))
                                    
MonthId =   str(currentMonth) + '_'+ str(currentYear)
dt = dtime.strptime(MonthId, '%m_%Y')                                  
print (MonthId,dt.month,dt.year)   
# dictionary
baseInfo = {MonthId:baseSeries }

# pandas DF
baseDF = pd.DataFrame(baseInfo)
print (baseDF)
print (baseDF.T)

## new try
emps = ['emp1','emp2']
months = ['08_2017','09_2017']
colIndex = flattenMixList (['MonthlySalary',
                                 dObj,
                                 'Advance Balance',
                                 'Balance For Month',
                                 'Total Salary'])

dataEntry = np.random.randint(10,size=(4,len(colIndex)))

allRows = pd.MultiIndex.from_tuples([ (x,y) for x in emps for y in months] )
newWayForRows = pd.MultiIndex.from_product([emps,months],names=['EmployeeName','Month'])
# dftry = pd.DataFrame(dataEntry,index=allRows ,columns=colIndex)
df2 = pd.DataFrame(dataEntry,index=newWayForRows ,columns=colIndex)
print (df2)

print (df2.xs('09_2017',level=1))




singleLineOfData = pd.DataFrame()