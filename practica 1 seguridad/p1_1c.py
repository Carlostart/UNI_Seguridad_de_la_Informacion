def cifradoCesarAlfabetoInglesMAY(cadena, num):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) + num) % 26) + 65
        elif (ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) + num) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado


def descifradoCesarAlfabetoInglesMAY(cadena, num):
    resultado = ''
    i = 0
    while i < len(cadena):
        ordenCifrado = ord(cadena[i])
        ordenClaro = 0
        if (ordenCifrado >= 65 and ordenCifrado <= 90):
            ordenClaro = (((ordenCifrado - 65) - num) % 26) + 65
        elif (ordenCifrado >= 97 and ordenCifrado <= 122):
            ordenClaro = (((ordenCifrado - 97) - num) % 26) + 97
        resultado = resultado + chr(ordenClaro)
        i = i + 1
    return resultado

claroCESAR = 'Veni Vidi Vinci Zeta'
numCesar = 5
print(claroCESAR)
cifradoCESAR = cifradoCesarAlfabetoInglesMAY(claroCESAR, numCesar) 
print(cifradoCESAR)
claroCESAR = descifradoCesarAlfabetoInglesMAY(cifradoCESAR, numCesar)
print(claroCESAR)
