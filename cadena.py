email="From rosario.titla@utpuebla.edu.mx Sat 5 jun 2020"
pos=email.find('@')
print(pos)
espacioPos=email.find(' ',pos)
print(espacioPos)
host=email[pos+1:espacioPos]
print(host)

ch1 = 'a'
ch2 = ' ' # espacio

print(ord(ch1))
print(ord(ch2))

# Demostrando la función chr()

print(chr(97))
print(chr(945))

# Indexando cadenas

exampleString = 'Rosario Titla'

for ix in range(len(exampleString)):
    print(exampleString[ix], end=' ')

print()

# Iterando a través de una cadena

exampleString = 'Jesus Flores'

for ch in exampleString:
    print(ch, end=' ')

print()

# Rodajas o rebanadas
alpha = "abdefg"
print(alpha[1:3])   #bd
print(alpha[3:])    #efg   a partir del 3er hasta el final
print(alpha[:3])    #abd  desde el inicio al 3er elemento
print(alpha[3:-2])  #e desde el 3er hasta el penúltimo
print(alpha[::2]) #adf desde el inicio hasta el final incremento de 2


# operador in   not in
alpfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" in alpfabeto)
print("F" in alpfabeto)
print("1" in alpfabeto)
print("ghi" in alpfabeto)
print("Xyz" in alpfabeto)


alfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alfabeto)
print("F" not in alfabeto)
print("1" not in alfabeto)
print("ghi" not in alfabeto)
print("Xyz" not in alfabeto)

#concatenar
alfabeto = "abcdefghijklmnopqrstuvwxy"

alfabeto = "Mi" + alfabeto
alfabeto = alfabeto + "z"

print(alfabeto)

# Demonstrando min() - Ejemplo 1
print(min(" aAbByYzZ")) #el espacio vacio es el min
print(min(" aAbByYzZ"))

# Demonstrando min() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡No!"'
print('[' + min(t) + ']')

lista = [0, 1, 2]
print(min(lista))

# Demostrando max() - Ejemplo 1
print(max("aAbByYzZ"))

# Demonstrando max() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡No!"'
print('[' + max(t) + ']')

listas = [0, 1, 2]
print(max(listas))

# Demonstrando el método index()
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demostrando la función list()
print(list("abcabc"))

# Demostrando el método count()
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Demostración del método capitalize()
print('aBcD'.capitalize())

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())



# Demostración del método center()
print('[' + 'alfa'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

#variante 2 parametros
print('[' + 'gamma'.center(20, '*') + ']')

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# Demostración del método endswith()
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

# Demostración del método find()
t = 'atleta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('te'))
print(t.find('ha'))

print('kappa'.find('a', 2))

txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)


#find 3 paramet
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))


# Demostración del método the isalnum() es alfanumerico
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# Ejemplo 1: Demostración del método isapha()
print("Moooo".isalpha())  #true
print('Mu40'.isalpha())   #false

# Ejemplo 2: Demostración del método isdigit()

print('2018'.isdigit())  #true
print("Año2019".isdigit())

# Ejemplo 1: Demostración del método islower()
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo 2: Demostración del método isspace()
print(' \n '.isspace()) # true
print(" ".isspace()) #true
print("mooo mooo mooo".isspace()) #false

# Ejemplo 3: Demostración del método isupper()
print("Moooo".isupper())  #false
print('moooo'.isupper())  #false
print('MOOOO'.isupper()) #true

