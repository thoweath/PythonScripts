from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series,DataFrame
import lxml

url = 'http://www.ucop.edu/operating-budget/budgets-and-reports/legislative-reports/2013-14-legislative-session.html'

#Request the content from the above url
result = requests.get(url)

c = result.content


#set as BeautifulSoup object
soup = BeautifulSoup(c,"lxml")

summary = soup.find('div',{'class':'span8 dotted-top','role':'main'})
tables = summary.find_all('table')

#this also works same as above, there is only 1 table element in above website
#tables = soup.find_all('table')

data = []
rows = tables[0].find_all('tr')


for tr in rows:
    cols = tr.find_all('td')
    for td in cols:
        text = td.find(text = True)
        data.append(text)

#print(data)

index = 0
reports = [item.replace('\xa0','') for item in data if 'pdf' in item]
date = []

for item in data:
    if 'pdf' in item:
        date.append(data[index-1])
    index += 1
# print(date)
# print(reports)

date = Series(date)
reports = Series(reports)

legislative_df = pd.concat([date,reports],axis=1)
legislative_df.columns = ['Date','Report']

print(legislative_df)
