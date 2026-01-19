#Estructura de datos: Lista

##Listas
mi_lista = [10, 'a', "cadena", 40, 50]
for_lista = [i for i in range(5)]

##metodos de listas
print("\n", mi_lista[1])#Accede al elemento en la posicion especificada

print("\n", mi_lista[-2])#Accede al penultimo elemento de la lista

print("\n", mi_lista.count(10))#Cuenta cuantas veces aparece un elemento en la lista

print("\n", mi_lista.index("cadena"))#Devuelve el indice de la primera aparicion del elemento especificado

mi_lista.append(5.96)#Agrega un elemento al final de la lista
print("\n", mi_lista)

mi_lista.remove('a')#Elimina el primer elemento con el valor especificado
mi_lista.remove("cadena")
print("\n", mi_lista)

mi_lista.insert(2, 68)#Inserta un elemento en la posicion especificada
print("\n", mi_lista, "\n")

print(mi_lista.pop())#Elimina y devuelve el ultimo elemento de la lista
print(mi_lista)

mi_lista.sort(reverse=True)#Ordena los elementos de la lista en orden descendente
#Aunque como condicion, todos los elementos deben ser del mismo tipo
print("\n", mi_lista)