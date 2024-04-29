nombre = "ejemplo"
print("Hola "+ nombre)

print("hola mnsd")

a = 10
b=2
c = a*b
print("valor es :", c)

nom1= "nmobre "
nom2=" otro dato"
nom3= nom1 + nom2
print (nom3)

#conjunto
conjunto ={"hola","otro nombre",1.89,"final"}
print("conjunto")
print(conjunto)


#lista
lista =["hola","otro nombre",1.89,"final"]
print("lista")
print(lista)
print(lista[2])
lista[2] = 1.75
print(lista)

#diccionario
diccionario ={
    'Nombre':"Cristian",
    'apellido':"Leon",
    'altura':1.5,
    'Edad':50
}
print(diccionario)
print(diccionario['altura'])
diccionario['altura'] =1.75
print(diccionario)


#promedios
otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_promedio=4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencia de duracion
diferencia_curso_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_curso_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_curso_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando porcentaje de tiempo vacio
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 //crudo_promedio /10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 //crudo_dalto /10

print (f'El curso de Dalto dura un {diferencia_curso_min}% menos que el más rápido')
print (f'El curso de Dalto dura un {diferencia_curso_max}% menos que el más lento')
print (f'El curso de Dalto dura un {diferencia_curso_promedio}% menos que el promedio')

#mosstrando lo removido
print (f'El curso promedio elimnina un {tiempo_vacio_promedio}% de tiempo vacio')
print (f'El curso elimnino un {tiempo_vacio_dalto}% de tiempo vacio')