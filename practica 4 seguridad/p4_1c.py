from Crypto.Hash import SHA256

file = open("file.txt",'w')
file.write("Jose Carlos\n")
file.write("Jiménez Albañir")
file.close()
file = open('file.txt', 'r')

f = file.read(4096)
print(f)

hash_object = SHA256.new(f.encode())
print(hash_object.digest())
file.close()
