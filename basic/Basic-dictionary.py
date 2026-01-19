#Estructura de datos: Diccionario

##Diccionario
mi_diccionario = {
    'nombre': 'Juan', 
    'edad': 30, 
    'ciudad': 'Madrid'
    }

print(mi_diccionario.keys())#Devuelve las claves del diccionario
print(mi_diccionario.values())#Devuelve los valores del diccionario
print(mi_diccionario.items())#Devuelve los pares clave-valor del diccionario

mi_diccionario.update({'edad': 31})
print("\n", mi_diccionario)#Actualiza el valor de la clave especificada