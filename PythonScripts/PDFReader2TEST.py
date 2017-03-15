"""
Parse text from PDF file.

Approach: Read PDF file into list, then use regex to find account number,
invoice number, bill date, due date and total due amount. Then write to csv file.
"""
import PyPDF2
import re
import csv
pdfFileObj = open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\TESTpdf.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
text = pageObj.extractText()
ls = []
ls = [item for item in list(text.split('\n'))]

accountNum = [a.strip() for a in ls if 'account number'.upper() in a.upper()]
invNum = [a for a in ls if 'invoice number'.upper() in a.upper()]
totDue = [a for a in ls if 'total current charges'.upper() in a.upper()]

def getAcctNum(ls):
    for a in ls:
        if re.findall('\d{9}[-]\d{5}',a):
            return re.findall('\d{9}[-]\d{5}',a)

def getInvNum(ls):
    for i in ls:
        if re.findall('\d{10}',i):
            return re.findall('\d{10}',i)

def getBillDate(ls):
    for i in ls:
        if re.findall('Bill\sDate\D+\s\d{2}[,]\s\d{4}',i):
            return re.findall('January\s\d{2}[,]\s\d{4}|February\s\d{2}[,]\s\d{4}|March\s\d{2}[,]\s\d{4}|April\s\d{2}[,]\s\d{4}|May\s\d{2}[,]\s\d{4}|June\s\d{2}[,]\s\d{4}|July\s\d{2}[,]\s\d{4}|August\s\d{2}[,]\s\d{4}|September\s\d{2}[,]\s\d{4}|October\s\d{2}[,]\s\d{4}|November\s\d{2}[,]\s\d{4}|December\s\d{2}[,]\s\d{4}',i)

def getDueDate(ls):
    for i in ls:
        if re.findall('Total\sAmount\sDue\sby\s\D+\s\d{2}[,]\s\d{4}',i):
            return re.findall('January\s\d{2}[,]\s\d{4}|February\s\d{2}[,]\s\d{4}|March\s\d{2}[,]\s\d{4}|April\s\d{2}[,]\s\d{4}|May\s\d{2}[,]\s\d{4}|June\s\d{2}[,]\s\d{4}|July\s\d{2}[,]\s\d{4}|August\s\d{2}[,]\s\d{4}|September\s\d{2}[,]\s\d{4}|October\s\d{2}[,]\s\d{4}|November\s\d{2}[,]\s\d{4}|December\s\d{2}[,]\s\d{4}',i)

totDueMatch = 0
def getTotDue(ls):
    for i in ls:
        if re.findall('[$]\d{3}[.]\d{2}',i):
            if totDueMatch == 0: # Optionally, totDueMatch declaration on line 36 and if stmt on this line could be moved to line 46
                return re.findall('[$]\d{3}[.]\d{2}',i)


accountNumMatch = ''.join(getAcctNum(accountNum))
invNumMatch = ''.join(getInvNum(invNum))
billDate = ''.join(getBillDate(ls))
totDueMatch = ''.join(getTotDue(ls))
dueDate = ''.join(getDueDate(ls))
#Debug
print(accountNumMatch)
print(invNumMatch)
print(billDate)
print(totDueMatch)
print(dueDate)


# def getTotDue(x):
# 	return float(''.join(num for num in x if num.isdigit() or num == '.'))
#
# def getAcctInvNmbr(x):
#     return int(''.join(num for num in x if num.isdigit()))

#NEXT STEP: output the relevant numbers for account, inv, and totDue to file
with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\extracted5.csv','w') as out_file:
    print('Writing file...')
    csvWriter = csv.writer(out_file,delimiter = ',')
    csvWriter.writerow(['Account Number','Invoice Number','Total Due','Bill Date','Due Date'])
    csvWriter.writerow([accountNumMatch, invNumMatch, totDueMatch, billDate, dueDate])

    # out_file.write('Account Number: ' + str(accountNumMatch[0]) + '\n')
    # out_file.write('Invoice Number: ' + str(invNumMatch[0]) + '\n')
    # out_file.write('Total Due: ' + str(totDueMatch[0]) + '\n')
    # out_file.write('Bill Date: ' + str(billDate[0]) + '\n')
    # out_file.write('Due Date: ' + str(dueDate[0]) + '\n')
