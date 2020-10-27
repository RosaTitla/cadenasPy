var = 2
print(var)    # salida: 2

def retVar():
    global var
    var = 5
    return var

print(retVar())    # salida: 5

print(var)    # salida: 5
