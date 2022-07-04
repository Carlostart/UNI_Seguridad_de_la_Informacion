from Crypto.Hash import SHA512

file = open("file.txt",'w')
file.write("Jose Carlos\n")
file.write("Jiménez Albañir")
file.close()
file = open('file.txt', 'r')

f = file.read()
print(f)

hash_object = SHA512.new(f.encode())
print(hash_object.digest())
file.close()
