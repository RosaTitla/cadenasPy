#What will the output be for the following code?
let = "z"
let_two = "p"
c = let_two + let
m = c*5
print(m)

song = "The rain in Spain..."
wds = song.split()
print(wds)

wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))
#Crea la lista lst1 y copia en ésta
# los elementos del 6 al 13 de la lista lst
# (ocho elementos en total)

lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]
output=lst[5:13]

#Cree la variable output y
# asígnale una lista cuyos
# elementos sean las palabras de la cadena str1
str1 = "OH THE PLACES YOU'LL GO"
output=str1.split()


#Write a program that extracts the last three items in the list sports and assigns it to the variable last. Make sure to write your code so that it works no matter how many items are in the list
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
longi=len(sports)
print(longi)
tres=longi-3
#last=sports[tres:]
last=sports[-3:]
print (last)

#Escriba un código que combine las siguientes
# variables para que la oración
# “You are doing a great job, keep it up!”
# "¡Está haciendo un gran trabajo, siga así!"
# se asigne  a la variable message.
# No edite los valores asignados a por, az, io o qy.
by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
message=" ".join([by,az,io,qy])
print(message)

# What will the output be for the following code?
ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)
#Yes, python is a zero-index based language and
# slices are inclusive of the first index
# and exclusive of the second.

#What is the type of m?
l = ['w', '7', 0, 9]
m = l[1:2]
print(type(m))

#What is the type of m?
l = ['w', '7', 0, 9]
m = l[1]
print(type(m))
#Yes, the quotes around the
# number mean that this is a string.

#What is the type of x?
b = "My, what a lovely day"
x = b.split(',')
#Yes, the .split() method returns a list.
#A. string B. integer C. float  D. list
#What is the type of a?
b = "My, what a lovely day"
x = b.split(',')
print(x)
z = "".join(x)
print(z)
y = z.split()
print(y)
a = "".join(y)
print(type(a))

#Write code to determine how many 9’s are in the list nums and assign that value to the variable how_many. Do not use a for loop to do this.
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
tot=nums.count(9)
print(tot)



#Escriba un código que use el slice (rodaja)
# para deshacerse del segundo 8 de modo
# que aquí solo haya dos 8 en la lista de la variable nums


nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
del nums[4:5]
print(nums)
#Asigne el último elemento de lst a la variable end_elem.
# Haga esto para que funcione sin importar el numero de elementos
# de la lista lst.
lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

#end_elem=lst[-1:]
end_elem=lst[len(lst)-1]
print(end_elem)

#Assign the number of elements in lst to the variable num_lst.
lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]
num_lst=len(lst)

#Create a variable called wrds and assign
# to it a list whose elements are the words in the string sent.
# Do not worry about punctuation.
sent = "The bicentennial for our university was in 2017"
wrds=sent.split()
print(wrds)


#add_str es una cadena con una lista de números separados por el signo +. Escriba código que use el patrón de acumulación para tomar la suma de todos los números y lo asigne a sum_val (un número entero). (Debería usar la función .split ("+") para dividir por "+" e int () para convertir a un número entero).


#addition_str is a string with a list of numbers
# separated by the + sign.
# Write code that uses the accumulation pattern
# to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).
addition_str = "2+5+10+20"
y=addition_str.split('+')
print(y)
sum_val=0
for x in y:
    sum_val+=int(x)
print(sum_val)


#que tipo de dato es a
b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)

#Write code that uses iteration to print out the length of each element of the list stored in str_list.
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
# Write your code here.
for str1 in str_list:
    print(len(str1))

#Para cada palabra de la lista de verbos,
# agregue una terminación -ing.
# Guarde esta nueva lista en una nueva lista, ing.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing=[]
for v in verbs:
    ing.append(v+'ing')
print(ing)






s = input("Enter some text")
ac = ""
for c in s:
    ac = ac + c + "-" + c + "-"
print(ac)
#imprime en forma inversa
s = "ball"
r = ""
for item in s:
   r = item.upper() + r
print(r)

#Para cada carácter de la cadena ya guardado en
# la variable str1, agregue cada carácter a
# una lista llamada chars

str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars=[]
for let in str1:
    if let!=" ":
        chars.append(let)
print(chars)

#Assign an empty string to the variable output.
# Using the range function, write code to make it
# so that the variable output has 35 a s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!
output1=""
for i in range(35):
    output1=output1+'a'
print(output1)


colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
colores=[]
for color in colors:
    if color[0] in ["A", "E", "I", "O", "U"]:
        colores.append(color)

print(colores)



#
# colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Purple", "Pink", "Brown", "Teal", "Turquois", "Peach", "Beige"]
# tot=len(colors)-1
# for position in range(tot):
#     color = colors[position]
#     print(color)
#     if color[0] in ["P", "B", "T"]:
#         del colors[position]
#         tot = len(colors) - 1
# print('lista',colors)

#agregar ing y guardarlo en la misma lista
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing=[]
for i in range(len(verbs)):
    verbs[i]=verbs[i]+'ing'
print(verbs)

#En la Universidad XYZ, las clases de matemáticas de nivel superior están numeradas de 300 en adelante. Las clases de inglés de nivel superior están numeradas desde 200 en adelante. Las clases de psicología de nivel superior son 400 en adelante. Crea dos listas, superior e inferior. Asigne cada curso de las clases a la lista correcta, superior o inferior. SUGERENCIA: recuerde, puede convertir algunas cadenas a diferentes tipos.

#Guardar y ejecutar


classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]

#La funcion keyword del módulo determina si una cadena es una palabra clave. p.ej. keyword.iskeyword (s) donde s es una cadena devolverá True o False, dependiendo de si la cadena es una palabra clave de Python o no. Importe el módulo de palabras clave y pruebe para ver si cada una de las palabras en la prueba de lista son palabras clave. Guarde las respuestas respectivas en una lista, keyword_test.
#The module keyword determines if a string is a keyword. e.g. keyword.iskeyword(s) where s is a string will return either True or False, depending on whether or not the string is a Python keyword. Import the keyword module and test to see whether each of the words in list test are keywords. Save the respective answers in a list, keyword_test.

def cyu(s1, s2):
   if len(s1) > len(s2):
      print(s1)
   else:
      print(s2)

cyu("Hello", "Goodbye")

def square(x):
    y = x * x
    print(y)   # Bad! This is confusing! Should use return instead!

toSquare = 10
squareResult = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, squareResult))
