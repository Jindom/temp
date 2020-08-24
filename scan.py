import urllib.request

with open("BT.lst") as f:
        lines = f.read().splitlines()
for line in lines:
        try:
                url = "http://" + line + ":888/pma"
                #print(url)
                response = urllib.request.urlopen(url,timeout=5)
                print(response.status)
        except:
                print(line +" skipped...")
                pass
