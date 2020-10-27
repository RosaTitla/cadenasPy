cad='turnovespertinogrupo'
print(cad[2])

for car in range(len(cad)):
    print(cad[car], end='\t')

print()
for el in cad:
    print(el,end='\t')
print()
#slice o rebanadas
cad1=cad[2:-2]
print(cad1)
if 'z' not in cad:
    print('no  se encuentra')
cade='bjke'
n=max(cade)
print('minimo',n)

pos=cad.index('n')
print(pos)
listaA=list(cad)
print(listaA)

cad2='turno,vespe, rtino,grupo'
print(cad2.endswith('po'))
print(cad2.isalpha())
print(cad2.isalnum())

listaE=cad2.split(',')
print(listaE)