from hashlib import md5, sha512
import base64

# x='b2D8A7EB96e0f5F3'
x = '03846600411'.encode('utf8')
# x='E46854B287555333'
md5_str = md5(x).hexdigest()
md5_str = ('7gbox3' + md5_str).encode('utf8')
sha512_str = sha512(md5_str)
sha512_str = sha512_str.digest()
signature = base64.b64encode(sha512_str).decode('utf8')
print(sha512_str)
print(signature)