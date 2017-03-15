from bs4 import BeautifulSoup
import requests
import lxml
import sqlite3

def makeSoup(url,parser):
    result = requests.get(url)
    c = result.content
    soup = BeautifulSoup(c,parser)
    return soup

def execQuery(sections):
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
            columnValues.append(None)
        try:
            col2 = col.findNext('div',{'class':'col'})
            notes = col2.find('dd').string
            columnValues.append(notes)
        except:
            columnValues.append(None)
        community = section.find('div',{'class':'action'})
        address = community.find('dd').string
        columnValues.append(address)
        #print(columnValues)
        yield columnValues

def crawl_url(soup):
    try:
        next_page = soup.find('li',{'class':'next'})
        url = next_page.find_all('a')
        for a in url:
            next_page = a.get('href')
            return next_page
    except:
        return False


def main():
    #site to scrape
    url = r'http://brickset.com/sets/year-2016'
    #make some soup
    soup = makeSoup(url,'lxml')
    sections = soup.find_all('article',{'class':'set'})

    #DEFINE TABLE
    db_name = r'C:\\Users\\tweatherall\\Desktop\\PDFScrapperDB2'
    table_name = 'Brickset'
    column1 = 'Title'
    column2 = 'Pieces'
    column3 = 'Minifigs'
    column4 = 'Notes'
    column5 = 'Address'
    text = 'TEXT'
    integer = 'INTEGER'

    #create database connection
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    #create table
    c.execute('CREATE TABLE IF NOT EXISTS {tn} ({cn1} {tp1}, {cn2} {tp2}, {cn3} {tp3}, {cn4} {tp4}, {cn5} {tp5})'.format(tn = table_name, cn1 = column1,
    tp1 = text, cn2=column2, tp2=integer, cn3 = column3, tp3 = integer, cn4=column4, tp4=text, cn5=column5, tp5=text))
    #create insert statement
    sql_insert = 'INSERT INTO {} VALUES (?,?,?,?,?)'.format(table_name)

    for set in execQuery(sections):
        c.execute(sql_insert,set)

    while crawl_url(soup):
        print('crawling page:',crawl_url(soup))
        soup = makeSoup(crawl_url(soup),'lxml')
        sections = soup.find_all('article',{'class':'set'})
        for set in execQuery(sections):
            c.execute(sql_insert,set)
        # test = soup.find('article',{'class':'set'})
        # print(test.find('h1'))

    #commit inserts
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
