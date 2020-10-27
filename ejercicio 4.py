# "{0} {1}".format(first, second)
first = "apple"
second = "banana"
third = "carrot"

formatted_string = "Frutas: {0}; {2};{1}".format(first, second, third)
print(formatted_string)
# apple carrot banana
nomProdu="tubo pvc de 3 pulgadas"
print('{:.3s}...'.format(nomProdu) )
#tubo ...
num=10.5
print('{:.2f}'.format(num) )




print('alineada al izq')
#string aligned to the left that many spaces
#cadena alineada a la izquierda tantos espacios
print("{:<25}".format(nomProdu))


#string aligned to the right that many spaces
#cadena alineada a la derecha tantos espacios
print('alineada al der')
print()
print("{:>25}".format(nomProdu))

def toCelcius(x):
    return (x-32)*5/9

for x in range( 0,101,10):
    print(str(x) +"->"+str(toCelcius(x)))

for x in range(0, 101, 10):
    print("{:>8}F  -> {:>10.2f}C".format(x,toCelcius(x)))