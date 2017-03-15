"""
Parse text from PDF file.

Approach: Read PDF file into list, then use regex to find account number,
invoice number, bill date, due date and total due amount. Then write to csv file
row by row for each page in pdf.
"""
import PyPDF2
import re
import csv

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

# Can use re.search to return regex match string (after using the .group() function) instead of returning regex match list, as re.findall does.
def getDueDate(ls):
    for i in ls:
        if re.search('Total\sAmount\sDue\sby\s\D+\s\d{2}[,]\s\d{4}',i):
            return re.search('January\s\d{2}[,]\s\d{4}|February\s\d{2}[,]\s\d{4}|March\s\d{2}[,]\s\d{4}|April\s\d{2}[,]\s\d{4}|May\s\d{2}[,]\s\d{4}|June\s\d{2}[,]\s\d{4}|July\s\d{2}[,]\s\d{4}|August\s\d{2}[,]\s\d{4}|September\s\d{2}[,]\s\d{4}|October\s\d{2}[,]\s\d{4}|November\s\d{2}[,]\s\d{4}|December\s\d{2}[,]\s\d{4}',i)

# def getTotDue(ls):
#     for i in ls:
#         if re.findall('[$]\d{3}[.]\d{2}',i):
#             if totDueMatch == 0: # use re.search here because there are multiple values that will be returned here, but re.search only returns the first match. So I do not need to use the totDueMatch == 0 conditional bit if I use re.search
#                 return re.findall('[$]\d{3}[.]\d{2}',i)
def getTotDue(ls):
    for i in ls:
        if re.search('[$]\d{3}[.]\d{2}',i):
            return re.search('[$]\d{3}[.]\d{2}',i)


def main():
    pdfFileObj = open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\VerizonBill.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    header = 0

    for i in list(range(pdfReader.getNumPages())):

        pageObj = pdfReader.getPage(i)
        text = pageObj.extractText()
        ls = []
        ls = [item for item in list(text.split('\n'))]

        accountNum = [a.strip() for a in ls if 'account number'.upper() in a.upper()]
        invNum = [a for a in ls if 'invoice number'.upper() in a.upper()]
        totDue = [a for a in ls if 'total current charges'.upper() in a.upper()]

        totDueMatch = 0

        accountNumMatch = ''.join(getAcctNum(accountNum))
        invNumMatch = ''.join(getInvNum(invNum))
        billDate = ''.join(getBillDate(ls))
        totDueMatch = getTotDue(ls).group() # use re.search here because re.findall would return multiple values, while re.search only returns first match
        dueDate = getDueDate(ls).group() # used re.search for this one, so need to use .group() function to return regex string
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

        #cannot use the with syntax while inside the for loop because it will close the file each iteration
        out_file = open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\extracted5.csv','a')
        print('Writing file...')
        if header == 0:
            csvWriter = csv.writer(out_file,delimiter = ',')
            csvWriter.writerow(['Account Number','Invoice Number','Total Due','Bill Date','Due Date'])
            header = 1
        csvWriter.writerow([accountNumMatch, invNumMatch, totDueMatch, billDate, dueDate])

            # out_file.write('Account Number: ' + str(accountNumMatch[0]) + '\n')
            # out_file.write('Invoice Number: ' + str(invNumMatch[0]) + '\n')
            # out_file.write('Total Due: ' + str(totDueMatch[0]) + '\n')
            # out_file.write('Bill Date: ' + str(billDate[0]) + '\n')
            # out_file.write('Due Date: ' + str(dueDate[0]) + '\n')
    out_file.close()

if __name__ == "__main__":
    main()
