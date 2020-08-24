import urllib.request
import threading

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}


with open("BT.lst") as f:
	lines = f.read().splitlines()
for line in lines:
	try:
		url = "http://" + line + ":888/pma"
		#print(url)
		response = urllib.request.urlopen(url,timeout=5,headers=headers)
		print(response.status)
	except:
		print(line +" skipped...")
		pass
