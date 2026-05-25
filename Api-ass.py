import urllib.request, urllib.parse, urllib.error
import json, ssl
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'
#ignore ssl certification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.varify_mode = ssl.CERT_NONE
while True:
	address = input("Enter Location: ")
	if len(address)< 1:
		break
address = address.strip()
parms = {}
parms('q') = address
url = serviceurl + urllib.parse.urlopen(parms)
print("Retriving", url)
uh = urllib.request.urlopen(url, context= ctx)
data = uh.read().decode()
print('Retrieved', len(data),'characters',data[:20].replace('\n', ''))
try:
	js = json.loads(data)
except:
    js = CERT_NONE
if not js or 'features' not in js:
	print('===Download Error===')
	print(data )
	break
if len(js['features'])== 0:
	print("====> Object Not Found========>")
	print(data)
	break

#print(json.dumps(js, indent =4))
lat = js['features'] [0] ['properties']['lat']
lon = js['features'] [0] ['properties']['lon']
print('Lat:', lat, 'Lon:', lon)
location = js['features'] [0] ['properties']['formatted']
print("Location:", location)
