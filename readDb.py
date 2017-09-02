import json


with open('database.db','r') as ff:
    
    importedData = json.load(ff)
    
print (importedData['emp1']['2_2017'])