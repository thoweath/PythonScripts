from bs4 import BeautifulSoup
import requests
import lxml
import sqlite3


url = r'http://brickset.com/sets/year-2016'

result = requests.get(url)
c = result.content
soup = BeautifulSoup(c,'lxml')
sections = soup.find_all('article',{'class':'set'})

db_name = r'C:\\Users\\tweatherall\\Desktop\\PDFScrapperDB2'
table_name = 'Brickset'
column1 = 'Title'
column2 = 'Pieces'
column3 = 'Minifigs'
text = 'TEXT'
integer = 'INTEGER'

#create database connection
conn = sqlite3.connect(db_name)
c = conn.cursor()
#create table
c.execute('CREATE TABLE IF NOT EXISTS {tn} ({cn1} {tp1}, {cn2} {tp2}, {cn3} {tp3})'.format(tn = table_name, cn1 = column1,
tp1 = text, cn2=column2, tp2=integer, cn3 = column3, tp3 = integer))
#create insert statement
sql_insert = 'INSERT INTO {} VALUES (?,?,?)'.format(table_name)


for section in sections:
    columnValues = []
    title = section.find('h1').string
    columnValues.append(title)
    col = section.find('div',{'class':'col'})
    pieces = col.find('dd').string
    columnValues.append(pieces)
    try:
        test = col.find('dt',string='Minifigs')
        minifigs = test.findNext('dd').string
        columnValues.append(minifigs)
    except:
        columnValues.append(0)
    #print(columnValues)
    c.execute(sql_insert,columnValues)

#commit inserts
conn.commit()
conn.close()


# db_name = r'C:\\Users\\tweatherall\\Desktop\\PDFScrapperDB2'
#
# table_name = 'PDFSCrappings'
#
# Col1 = 'UsageCharges'
# Col2 = 'Voice'
# Col3 = 'Messaging'
# Col4 = 'Data'
# Col5 = 'Taxes'
# Col6 = 'TaxesGovtSurcharges'
# Col7 = 'TotalCurrentCharges'
#
# colType = 'INTEGER'
#
# conn = sqlite3.connect(db_name)
# c = conn.cursor()
# c.execute('DROP TABLE {}'.format(table_name))
# c.execute('CREATE TABLE IF NOT EXISTS {tablename} ({Col1} {colType}, {Col2} {colType}, {Col3} {colType}, {Col4} {colType}, {Col5} {colType}, \
# {Col6} {colType}, {Col7} {colType})'.format(tablename=table_name,Col1=Col1,Col2=Col2,Col3=Col3,Col4=Col4,Col5=Col5,Col6=Col6,Col7=Col7,colType=colType))
# print(columnValues)
# testls = [9,9,9,9,9,9]
# sqlInsert = 'INSERT INTO PDFSCrappings VALUES (?,?,?,?,?,?,?)'
# c.execute(sqlInsert,columnValues)
# conn.commit()
# conn.close()
