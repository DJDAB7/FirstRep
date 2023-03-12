# Comentario linea sola
print ("Hello  world")  # Al final de la linea
#print ("Hello2 ")
print ("Hello3")
"""comentario multi lina 
o cadena de texto"""
nombre = "David"
edad = 39
estatura = 1.75
curso = True
otro = False
"""print(type(nombre))
print(type(edad))
print(type(estatura))
print(type(curso))"""
print("suma: ",edad+10)
print("division: ",edad/estatura)
print("cadena *: ",nombre*3)
print("boolean: ",edad>40)
print("igual a: ",edad==40)
print("Diferente de: ",edad!=40)
# -----------LISTAS---------------- #
lista = [7,9,3.75,True,"Hola",False,9]
print (lista)
print (lista[4])
print (len(lista))
print ("ultimo elemento: ",lista[-1])
print ("primer elemento: ",lista[-len(lista)])
print ("parte de lista: ",lista[1:4])
lista2 = [1,lista,"Valor"]
print (lista2)
print (lista2[1][3])
lista[3]="dime"
lista.append(True)
print (lista2)
lista3 = ["AA",3,"BB"]
lista4 = ["cA",35.74,"BB1"]
lista3.extend(lista)
print (lista3)
lista2.append(lista4)
print (lista2)
print(type(lista2))
print(type(lista2[1]))
print(type(lista2[0]))
# -----------TUPLAS---------------- #
tupla1 = ("AA",3,"BB")
tupla2 = "A3",2.75,"B1"
print (tupla1)
print (tupla2)
print(type(tupla1))
# -----------DICCIONARIOS---------------- #
dic1 = {
    'Nombre': 'David',
    'Apellido': 'De Abreu',
    'Edad': 39,
    'Estatura': 1.75,
    'Hobbies': ['Series','PC','Games']
}
print(dic1)
print(dic1['Nombre'])
dic1['Hijo']= "Gianluca De Abreu"
print(dic1)
print(dic1.items())
print(dic1.keys())
print(dic1.values())
# -----------SETS---------------- #
set1 = {2,1,"AA","BB"}
print(set1)
set1.add("New")
print(set1)
set1.update([1,3,"CC"])
print(set1)
tam = len(set1)
print(tam)
set1.remove("CC")  # SI NO ESTA DA ERROR
set1.discard("CC") # NO IMPORTA SI YA NO ESTA
print(set1)
set1.clear()
print(set1)