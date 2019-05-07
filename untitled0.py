
Report = []

_cont = True

while _cont:
  
    CustomerName = input("Name:")
    SaleAmount = input("Sale:")
    
    while True:
        cont = input("Continue ? [y/n]").lower()
        if cont in ('y','n'):
            break
    _cont = cont == 'y'
    
    Report.append(CustomerName+" ("+SaleAmount+") ")


index = (int)(0)
for item in Report: #use for loop to print data in the Hardware List
    index = index+1 # increase index number by 1 to print 1,2,3...
    print((str)(index)+". "+item+"\n")


    def _report(_report):
        report = []
        report.append(CustomerName)
        report.append(SaleAmount)   
        return report  

import json
import pandas as pd

file = 'Sample_matomo.json'

with open(file) as df_file:
    data = json.load(df_file)
    # print(data[0])

    custom_variable_list = []
    
    for raw in data:
        uuid = raw['visitorId']
        custom_variables = raw['customVariables']
        
        for cv in custom_variables:
            try:
                #t = (uuid, cv['customVariableName1'], cv['customVariableValue1'])
                t = (uuid)
                custom_variable_list.append(t)            
            except Exception as e:
                pass
                 
    df = df = pd.DataFrame(custom_variable_list)


        