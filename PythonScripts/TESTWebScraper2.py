"""
scrapes below URL for faculty and faculty phone numbers and constructs a
DataFrame containing both
"""


from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import requests
import pandas as pd
from pandas import Series,DataFrame
import lxml

url = 'http://www.ucop.edu/operating-budget/staff/index.html'

#Request the content from the above url
result = requests.get(url)

c = result.content

#set as BeautifulSoup object
soup = BeautifulSoup(c,"html5lib")

summary = soup.find('div',{'class':'span8','role':'main'})
faculty = summary.find_all('h3',{'class':'blue'})
facultyClean = [fac.string for fac in faculty]
print(facultyClean)
# for fac in faculty:
#     print(fac.string)

facultyPhone = [phone.string for phone in summary.find_all('p')]
toReplace = [r'\n','None']
tempPhones = []
for p in facultyPhone:
    if 'None' in str(p):
        tempPhones.append(str(p).replace('None','').strip())
    else:
        tempPhones.append(str(p).strip())
    #print(clean.strip())
cleanPhones = [p for p in tempPhones if p != '']

def cleanList(ls):
    cleanPhones2 = []
    for p in cleanPhones:
        temp = []
        temp += p.split(':')
        for item in temp:
            if item != 'Phone':
                cleanPhones2.append(item.strip())
    return cleanPhones2
#cleanPhones2 = [p.split(':') for p in cleanPhones]

seriesFaculty = Series(facultyClean)
seriesFacPhone = Series(cleanList(cleanPhones))

facPhone_df = pd.concat([seriesFaculty,seriesFacPhone],axis=1)
facPhone_df.columns = ['Faculty','Phone']

print(facPhone_df)
    # temp = str(p).replace(r'\n','')
    # temp2 = str(temp).replace('None','')
    #print(temp2)
#print(facultyPhone)

# tables = prettySoup.find_all('table',{'class':'wikitable sortable jquery-tablesorter'})
# print(tables)

# data = []
# rows = tables[0].find_all('tr')


# for tr in rows:
#     cols = tr.find_all('td')
#     for td in cols:
#         text = td.find(text = True)
#         data.append(text)
#
# #print(data)
#
# index = 0
# reports = [item.replace('\xa0','') for item in data if 'pdf' in item]
# date = []
#
# for item in data:
#     if 'pdf' in item:
#         date.append(data[index-1])
#     index += 1
# # print(date)
# # print(reports)
#
# date = Series(date)
# reports = Series(reports)
#
# legislative_df = pd.concat([date,reports],axis=1)
# legislative_df.columns = ['Date','Report']
#
# print(legislative_df)
