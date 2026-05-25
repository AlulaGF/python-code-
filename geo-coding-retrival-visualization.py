import urllib.request,urllib.parse, urllib.error
import http
import json
import sqlite3
import time
import ssl
import sys
#https://
serviceurl = "Input my open geo ....."
#additional details for urllib
#http.client.HTTPConnection.debuglevel = 1
conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations(address TEXT, geodata TEXT)''' )
#Ignore SSl Certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.varify_mode = ssl.CERT_NONE

fn = open("where.data")
count = 0
nofound = 0
for line in fn:
	if count > 100:
		print('Retrieved 100 locations, restart to retrieve more')
		break
	address = line.strip()
    print(' ')
    cur.execute("SELECT geodata FROM Locations WHERE address = ?", (memoryviw(address.encode()),))
    try:
    	data = cur.fetchone()[0]
    	print("Fond in database", address)
    	continue
    except:
    	pass

    parms = {}
    parms['q'] = address
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retriving', url)
    uh = urllib.requset.urlopen(url, cont
    print('Retriving', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1
    try:
    	js = json.loads(dat)
    except:
    	print(data) # print to makesure incase unicode makes error
    	continue

    if not js or 'features' not in js:
    	print('===Download erro===')
    	print(data)ext=ctx)
    data = uh.read().decode()
    	break
    if len(js['features'])== 0:
    	print('===object not found===')
    	nofound = nofound + 1

    cur.execute(''' INSERT INTO Locatons (address, geodata) VALUES(?,?)''',(memoryviw(address.encode()), memoryviw(data.encode())))

    conn.commit()
    if count % 10 == 0:
    	print('pausing for a bit...')
    	time.sleep(5)

    if nofound > 0:
    	print("Number of features for which the location could not be found:" , nofound)


