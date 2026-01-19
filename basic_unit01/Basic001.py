#iniciacion
print("hello world")

#tipos de datos
##int
a = 5
##float
b = 3.14
## string
c = "Hello"
##bool
d = True



#funciones
def aritmetica(x, y):
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    potenciacion = x ** y
    division = x / y
    division_entera = x // y
    modulo = x % y #resto de la division
    return suma, resta, multiplicacion, potenciacion, division, division_entera, modulo

resultado = aritmetica(10, 3)
print(resultado)