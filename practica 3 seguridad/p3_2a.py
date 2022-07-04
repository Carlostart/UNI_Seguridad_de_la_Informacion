import p3_1 as RSA

password = "password"
private_file = "rsa_key.pem"
public_file = "rsa_key.pub"
A = RSA.RSA_OBJECT()
A.create_KeyPair()
B = RSA.RSA_OBJECT()
B.create_KeyPair()
c = B.cifrar("Hola Amigos de la Seguridad".encode("utf-8"))
s = A.firmar(c)

if A.comprobar(c, s):
    print("La firma es valida")
else:
    print("La firma es invalida")
