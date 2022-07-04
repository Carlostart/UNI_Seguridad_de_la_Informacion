from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64

class AES_CIPHER:
    BLOCK_SIZE_AES = 16 # DES: Bloque de 64 bits

    def __init__(self, key):
        """Inicializa las variables locales"""
        self.key = key

    def cifrar(self, cadena, IV):
        """Cifra el parámetro cadena (de tipo String) con una IV específica, y
        devuelve el texto cifrado binario"""
        cipher=AES.new(self.key, AES.MODE_CBC, IV)
        cadena = cadena.encode('utf-8')
        return cipher.encrypt(pad(cadena, self.BLOCK_SIZE_AES))

    def descifrar(self, cifrado, IV):
        """Descrifra el parámetro cifrado (de tipo binario) con una IV específica, y
        devuelve la cadena en claro de tipo String"""
        decipher_aes = AES.new(self.key, AES.MODE_CBC, IV)
        return unpad(decipher_aes.decrypt(cifrado), self.BLOCK_SIZE_AES).decode("utf-8", "ignore")



key = get_random_bytes(16) # Clave aleatoria de 64 bits
IV = get_random_bytes(16) # IV aleatorio de 64 bits
datos = "Hola Mundo con DES en modo CBC"
d = AES_CIPHER(key)
cifrado = d.cifrar(datos, IV)
descifrado = d.descifrar(cifrado, IV)

print(datos)

print(cifrado)
encoded_ciphertext = base64.b64encode(cifrado)
print(encoded_ciphertext)

print(descifrado)
