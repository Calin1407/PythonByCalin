c = "Hello"
a = 5
d = True

#bucles
for i in c:
    print(i)

print("|||||||||||||||||||||||||||||||||||||||||||")

while a < 1:
    print(a)
    a -= 1

print("|||||||||||||||||||||||||||||||||||||||||||")

#Control de bucles
while d:
    print("Se rompe bucle por break")
    break

print("|||||||||||||||||||||||||||||||||||||||||||")

for i in range(10):
    if i % 2 == 0:
        print("Numero par, se salta")
        continue
    print(i)

print("|||||||||||||||||||||||||||||||||||||||||||")

for i in range(5):
    if i == 3:
        pass #placeholder, no hace nada
    else:
        print(i)