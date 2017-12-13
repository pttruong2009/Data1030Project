import urllib3, sys
import json
from pymongo import MongoClient
a = []
#Calling database on mLab
client = MongoClient('mongodb://cavu17:Hello1234@ds111476.mlab.com:11476/final_project')
db = client.get_database('final_project')

#Scraping 10,000 pages through Linked-In API, 200 pages at a time
#Note: this code doesn't work as well anymore because the token has expired
for x in range(200):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(201, 400):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(401, 600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(601, 800):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(801, 1000):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(1001, 1200):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(1201, 1400):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(1401, 1600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(1601, 1800):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(1801, 2000):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(2001, 2200):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(2201, 2400):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(2401, 2600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(2601, 2800):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(2801, 3000):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(3001, 3200):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(3201, 3400):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(3401, 3600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(3601, 3800):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(3801, 4000):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(4001, 4200):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(4201, 4400):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(4401, 4600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(4601, 4800):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(4801, 5000):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(5001, 5200):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(5201, 5400):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(5401, 5600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(5601, 5800):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(5801, 6000):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(6001, 6200):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(6201, 6400):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(6401, 6600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(6601, 6800):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(6801, 7000):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(7001, 7200):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(i)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(7201, 7400):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(7401, 7600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(7601, 7800):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(7801, 8000):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(8001, 8200):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(8201, 8400):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(i)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(8401, 8600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(8601, 8800):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(8801, 9000):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(9001, 9200):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(9201, 9400):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(9401, 9600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(9401, 9600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(9401, 9600):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(9601, 9800):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

for x in range(9801, 10000):
    http = urllib3.PoolManager()
    request = 'http://api.glassdoor.com/api/api.htm?t.p=226249&t.k=blWye0Bi7tS&userip=138.16.123.48&useragent=&format=json&v=1&action=employers'
    request = request + '&pn=' + str(x)
    r = http.request('GET', request)
    r = json.loads(r.data.decode('utf-8'))
    a = a + r['response']['employers']

#Inputting the data into the database called "glassdoor_all_backup"
for i in range(len(a)):
    company = a[i]
    db.glassdoor_all_backup.insert_one(company)

#checking stats
# print(db.command("dbstats"))
# print(db.command('listCollections'))

#Putting it in a csv and putting filters for further analysis

names = []
culture_rating = []
compensation_rating = []
overallRating = []
ratingDescription = [] # Need to make this one hot code maybe?? or make it numerical
recommendToFriendRating = []
seniorLeadershipRating = []
workLifeBalanceRating = []
ceo_names = []
ceo_pctApprove = []
ceo_pctDisapprove = []
sector_name = []
industry = []

names = [a[i]['name'] for i in range(len(a))]
culture_rating = [a[i]['cultureAndValuesRating'] for i in range(len(a))]
compensation_rating = [a[i]['compensationAndBenefitsRating'] for i in range(len(a))]
overallRating = [a[i]['overallRating'] for i in range(len(a))]
ratingDescription = [a[i]['ratingDescription'] for i in range(len(a))] # Need to make this one hot code maybe?? or make it numerical
recommendToFriendRating = [a[i]['recommendToFriendRating'] for i in range(len(a))]
seniorLeadershipRating = [a[i]['seniorLeadershipRating'] for i in range(len(a))]
workLifeBalanceRating = [a[i]['workLifeBalanceRating'] for i in range(len(a))]

for i in range(len(a)):
    try:
        ceo_names.append(a[i]['ceo']['name'])
    except:
        ceo_names.append(None)

for i in range(len(a)):
    try:
        ceo_pctApprove.append(a[i]['ceo']['pctApprove'])
    except:
        ceo_pctApprove.append(None)

for i in range(len(a)):
    try:
        ceo_pctDisapprove.append(a[i]['ceo']['pctDisapprove'])
    except:
        ceo_pctDisapprove.append(None)
for i in range(len(a)):
    try:
        sector_name.append(a[i]['sectorName'])
    except:
        sector_name.append(None)
for i in range(len(a)):
    try:
        industry.append(a[i]['industry'])
    except:
        industry.append(None)

df = pd.DataFrame({'company_name': names,
                   'culture_rating':culture_rating,
                  'compensation_rating':compensation_rating,
                  'overallRating':overallRating,
                  'ratingDescription':ratingDescription,
                  'recommendToFriendRating': recommendToFriendRating,
                  'seniorLeadershipRating': seniorLeadershipRating,
                  'workLifeBalanceRating': workLifeBalanceRating,
                  'ceo_names': ceo_names,
                  'ceo_pctApprove':ceo_pctApprove,
                  'ceo_pctDisapprove':ceo_pctDisapprove,
                  'industry':industry,
                  'sector_name':sector_name})
df = df.drop_duplicates(keep = 'first')
df.to_csv('glass_door_all_10_filtered.csv')