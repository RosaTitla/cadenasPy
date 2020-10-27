cadena='joe 10 15 20 30 40'
listaCalif=cadena.split(' ')
print(listaCalif)
miLetra='b'
print(ord(miLetra))

print(chr(97))

contraseñaCifrada=''
contraseña='puebla'
for letra in contraseña:
    cod=ord(letra)
    cifrado=cod+1
    nuevaLetra=chr(cifrado)
    contraseñaCifrada=contraseñaCifrada+nuevaLetra
print(contraseñaCifrada)


