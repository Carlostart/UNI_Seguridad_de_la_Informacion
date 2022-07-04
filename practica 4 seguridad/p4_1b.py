from Crypto.Hash import HMAC, SHA512

file = open("file.txt",'w')
file.write("Jose Carlos\n")
file.write("Jiménez Albañir")
file.close()
file = open('file.txt', 'r')
f = file.read()
file.close()
print(f)

secret = b'S3cr3tk3y'
h = HMAC.new(secret, f.encode(), digestmod=SHA512)
d = h.digest()
h.verify(d)
print(d)
