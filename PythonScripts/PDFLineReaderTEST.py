from PyPDF2 import PdfFileReader
import csv
from pandas import DataFrame

def get_pdf_content_lines(pdf_file_path):
    with open(pdf_file_path,'rb') as f:
        pdf_reader = PdfFileReader(f)
        for page in pdf_reader.pages:
            for line in page.extractText().split('\n'):
                yield line

#get_pdf_content_lines(r'C:\\Users\\tweatherall\\Desktop\\TestPDFDir\\VerizonBill.pdf')

for line in get_pdf_content_lines(r'C:\\Users\\tweatherall\\Desktop\\TestPDFDir\\ExcelPDFxlsx.pdf'):
    with open(r'C:\\Users\\tweatherall\\Desktop\\TestPDFDir\\extractedPDF.csv','a') as out_file:
        csvWriter = csv.writer(out_file)
        print(line)
        csvWriter.writerow([line])
