# Estructura de datos

##set
frutas = {"manzana", "banana", "cereza"}
numeros = set([1, 2, 3, 4, 5])

##set se utiliza para almacenar elementos únicos y no ordenados
##en otras palabras, interpretamos que es un conjunto matemático
##los elementos pueden tratarse con los conceptos como unión, intersección, diferencia, etc.

##operaciones con set
###UNION
conjuntoA = {1, 2, 3}
conjuntoB = {3, 4, 5}
union = conjuntoA & conjuntoB
print("Unión:", union)  # Salida: Unión: {3}-

###INTERSECCIÓN
interseccion = conjuntoA | conjuntoB
print("Intersección:", interseccion)  # Salida: Intersección:

###DIFERENCIA
diferencia = conjuntoA - conjuntoB
print("Diferencia:", diferencia)  # Salida: Diferencia: {1, 2}

###DIFERENCIA SIMÉTRICA
diferencia_simetrica = conjuntoA ^ conjuntoB
print("Diferencia Simétrica:", diferencia_simetrica)  # Salida: Diferencia Simétrica: {1, 2, 4, 5}

##métodos comunes
###Agregar un elemento
frutas.add("naranja")
print("Frutas después de agregar naranja:", frutas)
###Eliminar un elemento
frutas.remove("banana")
print("Frutas después de eliminar banana:", frutas)
###Verificar si un elemento está en el set
existe_manzana = "manzana" in frutas
print("¿Existe manzana en frutas?", existe_manzana)
###Longitud del set
longitud_frutas = len(frutas)
print("Número de frutas:", longitud_frutas)