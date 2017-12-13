import requests
from bs4 import BeautifulSoup
import pandas as pd
#Scraping all the company names through the search engine of Indeed
r = requests.get('https://www.indeed.com/cmp?')
final = []
final2 = []
lst = ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y','z']
for item in lst:
    for page in range(2,100):
        r ='https://www.indeed.com/cmp?q=' + item +'&p=' + str(page)
        r = requests.get(r)
        soup = BeautifulSoup(r.text, 'lxml')
        try:
            soup1 = soup.find_all('div')[4]
        except:
            break
        for i in range(0,9):
            try:
                soup2 = soup1.find_all(class_="company_result_title")[i]
                final.append(soup2.a['href'])
            except:
                break
#Since we went through the alphabet, remove some repeats
myset = set(final)
myset2= list(myset)

#Get the HQ location from sidebar if exists
for i in myset2:
    r = 'https://www.indeed.com' + i
    r = requests.get(r)
    soup = BeautifulSoup(r.text,'lxml')
    soup1 = soup.find_all('div')[4]
    soup2 = soup1.find_all(class_="cmp-dl-list-big cmp-sidebar-section cmp-bordered-box")
    try:
        soup3 = soup2[0].find('dd')
        final2.append(soup3.getText())
    except:
        final2.append(None)

split = [i.split('/cmp/', 1)[1] for i in myset2]
address = pd.DataFrame(split)
address['address'] = pd.Series(final2)
address = address.dropna(axis = 0)
address.to_csv('indeed_addresses.csv')