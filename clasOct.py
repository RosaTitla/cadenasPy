cadena='joe 10 15 20 30 40'
#split  gen lista

lista22=cadena.split(' ')
print(lista22)
contraseñaCifrada=''
contraseña='puebla'
for el in contraseña:
    cod=ord(el)  #p   112
    codi=cod+2  #114
    letra=chr(codi)
    #print(letra)
    contraseñaCifrada=contraseñaCifrada+letra
print(contraseñaCifrada)
contraseñaDesCifrada=''
for ele in contraseñaCifrada:
   codigo=ord(ele)
   c=codigo-2
   letraDescifrada=chr(c)
   contraseñaDesCifrada=contraseñaDesCifrada+letraDescifrada
print(contraseñaDesCifrada)