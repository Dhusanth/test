
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
    