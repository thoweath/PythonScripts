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

def makeSoup(url,parser):
    #Request the content from the above url
    result = requests.get(url)
    c = result.content
    #set as BeautifulSoup object
    soup = BeautifulSoup(c,parser)
    return soup

soup = makeSoup(url,'lxml')

summary = soup.find('div',{'class':'span8','role':'main'})
faculty = summary.find_all('h3',{'class':'blue'})
facultyClean = [fac.string for fac in faculty]
#print(facultyClean)
# for fac in faculty:
#     print(fac.string)

facultyPhone = [phone.string for phone in summary.find_all('p')]
def replaceVals(phoneList,*charToReplace):
    #toReplace = charToReplace
    tempPhones = []
    for p in facultyPhone:
        for ch in charToReplace:
            if ch in str(p):
                tempPhones.append(str(p).replace(ch,'').strip())
            else:
                tempPhones.append(str(p).strip())
            #print(clean.strip())
    cleanPhones = [p for p in tempPhones if p != '']
    return cleanPhones

cleanPhones = replaceVals(facultyPhone,'None')

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
