# cadena='joe,10 15,20,30,40'
# lista=cadena.split(',')
# print(lista)


miLetra='j'
print(ord(miLetra))
print(chr(97))

contraseñaEncriptada=''
contraseña='jalisco'
for letra in contraseña:
    cod=ord(letra)
    print(cod)
    codi=cod+6//2-4
    letraCifrada=chr(codi)
    contraseñaEncriptada=contraseñaEncriptada+letraCifrada
print(contraseñaEncriptada)

contraseñaDecifrada=''
for let in contraseñaEncriptada:
    c=ord(let)
    co=c+4*2-6-1
    print(co)
    letraDescifrada=chr(co)

    contraseñaDecifrada=contraseñaDecifrada+letraDescifrada
print('decifrada',contraseñaDecifrada)




