
ventajas='''
1 Automatiza los procesos .-La Inteligencia artificial permite que robots desarrollen tareas repetitivas, rutinarias y de optimización de procesos de una manera automática y sin intervención humana.
2 Potencia las tareas creativas.-La IA libera a las personas de tareas rutinarias y repetitivas y permite que estas puedan destinar más tiempo a desarrollar funciones creativas.
3 Aporta precisión.-La aplicación de la IA  es capaz de aportar una precisión mayor que el ser humano, por ejemplo en entornos industriales, las máquinas pueden llegar a tomar decisiones que antes sin la IA se tomaban de manera manual o monitorizada.
4 Reduce el error humano.-La IA reduce los fallos provocados por las limitaciones del ser humano. En algunas cadenas de producción la IA se utiliza para detectar mediante sensores de infrarrojos, pequeñas fisuras o defectos en piezas que son indetectables por el ojo humano.
5 Reduce los tiempos empleados en análisis de datos.-Permite que el análisis y la explotación de los datos derivados de producción se  puedan llegar a efectúear en tiempo real.
6 Mantenimiento predictivo.-Permite realizar un mantenimiento del equipamiento industrial basado en los tiempos y condiciones de funcionamiento de los mismos, permitiendo incrementar su rendimiento y ciclo de vida.
7 Mejora en la toma de decisiones tanto a nivel de producción como de negocio.-Al disponer de mayor información de una manera estructurada, permite a cada uno de los responsables tomar decisiones de una manera más rápida y eficiente.
8 Control y optimización de procesos productivos y líneas de producción.-A través de la IA se consiguen procesos más eficientes, libres de errores, obteniendo mayor control sobre las líneas de producción en la empresa.
9 Aumento de la productividad y calidad en la producción.-La IA no sólo incrementa la productividad a nivel de maquinaria, sino que también hace que incremente la productividad de los trabajadores y la calidad del trabajo que realizan. El poder gozar de mayor información, les permite tener una visión más focalizada de su trabajo y tomar mejores decisiones.

'''
lstVentajas=[]
#lstVentajas=ventajas.split('.-')
numeros=['1','2','3','4','5','6','7','8','9']
for num in numeros:
   posIni=ventajas.find(num)
   posFin=ventajas.find('.-',posIni)
   cadena=ventajas[posIni:posFin]
   print(cadena)
   #lstVentajas=lstVentajas.append(cadena)

print(lstVentajas)


#ejercicio 1
email="From rosario.titla@utpuebla.edu.mx Sat 5 jun 2020"
pos=email.find('@')
print(pos)
espacioPos=email.find(' ',pos)
print(espacioPos)
host=email[pos+1:espacioPos]
print(host)


new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
sub_lst=new_lst[8:12]
print (sub_lst)