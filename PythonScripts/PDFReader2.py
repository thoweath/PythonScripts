"""
Parse text from PDF file.

Approach: Read PDF into list, then search list for certain terms. Append lines
where terms are found to new file or list, then parse those lines for the info

394.22
26572588200001
1503541657
"""


def getTotDue(x):
	return float(''.join(num for num in x if num.isdigit() or num == '.'))

def getAcctInvNmbr(x):
    return int(''.join(num for num in x if num.isdigit()))


def main(pdfName,filename,totalDue,accountNumber,invoiceNumber):
    pdfFileObj = open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\' + pdfName,'rb')
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
            accountNum += item.split()
        if 'invoice number'.upper() in item.upper():
            #print(item)
            #invNum.append(item)
            invNum += item.split()
        if 'total current charges'.upper() in item.upper():
            #totDue.append(item.split())
            totDue += item.split()

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


    with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\' + filename,'w') as out_file:
        #try:
        print('Writing file...')
        for item in nmbr:
            if item == float(totalDue):
                print(item)
                out_file.write('Total Due: ')
                out_file.write(str(item))
                out_file.write('\n')
        for item in AcctNmbr:
            if item == int(accountNumber):
                print(item)
                out_file.write('Account Number: ' + str(item))
                out_file.write('\n')
        for item in InvNmbr:
            if item == int(invoiceNumber):
                print(item)
                out_file.write('Invoice Number: ' + str(item))
                out_file.write('\n')
        # except:
        #     print('EOF reached')



if __name__ == "__main__":
    import PyPDF2
    import re
    pdfFile = input('Enter PDF to parse:')
    outFile = input('Enter output file name:')
    totalDue = input('Enter total due amount:')
    accountNumber = input('Enter account number:')
    invoiceNumber = input('Enter invoice number:')
    main(pdfFile,outFile,totalDue,accountNumber,invoiceNumber)
