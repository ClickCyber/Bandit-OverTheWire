import requests, bs4, hashlib

router = 'http://206.189.18.74:30977/'
found = True
res = requests.Session()

def send_md5():
    global found
    slice = bs4.BeautifulSoup(res.get(router).text, 'html.parser')
    md5 = hashlib.md5(slice.find('h3').text.encode()).hexdigest()
    results = res.post(router, data={'hash':md5})
    if 'HTB' in results.text:
        found = False
        slice = bs4.BeautifulSoup(results.text, 'html.parser')
        print(f"[+] {slice.find('p').text}")
        
if __name__ == "__main__":
    while found:
        send_md5()
# HTB{N1c3_ScrIpt1nG_B0i!}
