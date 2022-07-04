from Crypto.Cipher import PKCS1_OAEP, DES, AES
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256, HMAC
from Crypto.Signature import pss
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import base64
import json
from socket_class import SOCKET_SIMPLE_TCP

key_b_t = b'FEDCBA9876543210'
BLOCK_SIZE_AES = 16

socket = SOCKET_SIMPLE_TCP('127.0.0.2', 5555)   # Crea conexion con alice
socket.escuchar()                               # Escucha lo que a envia
datos = socket.recibir()
datos = datos.decode('utf-8')

decipher_aes_b_t = AES.new(key_b_t, AES.MODE_ECB)
json_t_a = unpad(decipher_aes_b_t.decrypt(bytearray.fromhex(datos)), BLOCK_SIZE_AES).decode("utf-8")


key_a_b = bytearray.fromhex(json.loads(json_t_a)[0])

a_random = get_random_bytes(8)                  # Generamos la clave

rnd = a_random.hex()
print('Random: ' + rnd)
cipher_aes_a_b = AES.new(key_a_b, AES.MODE_ECB)
rnd_enc = cipher_aes_a_b.encrypt(pad(rnd.encode("utf-8"),BLOCK_SIZE_AES))

socket.enviar(rnd_enc)                         # Enviamos el json a alice

datos = socket.recibir()
decipher_aes_a_b = AES.new(key_a_b, AES.MODE_ECB)
msg_a_b = unpad(decipher_aes_a_b.decrypt(datos), BLOCK_SIZE_AES).decode("utf-8")

print('Devuelto:',msg_a_b)

socket.cerrar()