led1 = [
['###', '# #', '# #', '# #', '###'],
[' #', ' #', ' #', ' #', ' #'],
['###', '  #', '###', '#  ', '###'],
['###', '  #', '###', '  #', '###'],
['# #', '# #', '###', '  #', '  #'],
['###', '# ', '###', '  #', '###'],
['###', '# ', '###', '# #', '###'],
['###', '  #', '  #', '  #', '  #'],
['###', '# #', '###', '# #', '###'],
['###', '# #', '###', '  #', '###']]


var = int(input("Ingrese el número a mostrar: "))
digitos = [led1[int(digito)] for digito in str(var)]

for i in range(5):
    print(" ".join(segmento[i] for segmento in digitos))
