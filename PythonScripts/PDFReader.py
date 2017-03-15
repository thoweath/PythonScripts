"""
Parse text from PDF file.

Approach: Read PDF into list, then search list for certain terms. Append lines
where terms are found to new file or list, then parse those lines for the info
"""
import PyPDF2
import re
pdfFileObj = open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\TESTpdf.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
text = pageObj.extractText()
ls = [item.strip() for item in list(text.split('\n'))]

accountNum = []
invNum = []
totDue = []
for item in ls:
    if 'account number'.upper() in item.upper():
        #print(item)
        #accountNum.append(item)
        accountNum += item.split()s
    if 'invoice number'.upper() in item.upper():
        #print(item)
        #invNum.append(item)
        invNum += item.split()
    if 'total current charges'.upper() in item.upper():
        #totDue.append(item.split())
        totDue += item.split()

def getTotDue(x):
	return float(''.join(num for num in x if num.isdigit() or num == '.'))

def getAcctInvNmbr(x):
    return int(''.join(num for num in x if num.isdigit()))

nmbr = [] #holds list of numbers in totDue list
for item in totDue:
    try:
        nmbr.append(getTotDue(item))
    except:
        continue

AcctNmbr = [] #holds list of numbers in accountNum list
for account in accountNum:
    try:
        AcctNmbr.append(getAcctInvNmbr(account))
    except:
        continue

InvNmbr = [] #holds list of numbers in invNum list
for invoice in invNum:
    try:
        InvNmbr.append(getAcctInvNmbr(invoice))
    except:
        continue

#NEXT STEP: output the relevant numbers for account, inv, and totDue to file
with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\extracted5.txt','w') as out_file:
    try:
        print('Writing file...')
        for item in nmbr:
            if item == float('394.22'):
                print(item)
                out_file.write('Total Due: ')
                out_file.write(str(item))
                out_file.write('\n')
        for item in AcctNmbr:
            if item == int('26572588200001'):
                print(item)
                out_file.write('Account Number: ' + str(item))
                out_file.write('\n')
        for item in InvNmbr:
            if item == int('1503541657'):
                print(item)
                out_file.write('Invoice Number: ' + str(item))
                out_file.write('\n')
    except:
        print('EOF reached')
