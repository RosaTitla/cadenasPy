email=['UTP0140477','UTP0143610','UTP0139965','UTP0139754','UTP0142302','UTP0143293','UTP0142814','UTP0142081','UTP0140516']
correos=[]

for z in email:
    m=z.swapcase()
    correo=m+"@utpuebla.edu.mx"
    correos.append(correo)
print(correos)
#https://pypi.org/search/?q=cimage&o=
#instal pip instalador de paquetes
#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
