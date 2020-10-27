email="From rosario.titla@utpuebla.edu.mx Sat 5 jun 2020"
pos=email.find('@')
print(pos)
espacioPos=email.find(' ',pos)
print(espacioPos)
host=email[pos+1:espacioPos]
print(host)


txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s
or earlier, when it was popularized by advertisements
for Letraset transfer sheets. It was introduced to
 the Information Age in the mid-1980s by the Aldus Corporation,
 which employed it in graphics and word-processing templates
 for its desktop publishing program PageMaker (from Wikipedia)"""
c=0
fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    c+=1
    fnd = txt.find('the', fnd + 3)
print("total de veces encontrada la palabra the: ",c)