#Adivina el numero
import random

print("==================================")
print("       Adivina el numero")         
print("==================================")

randomNum  = random.randrange(0,101)
thinkNum = ""

print("En que numero estoy pensando?")
print("")
thinkNum = int(input("Ingrese el numero: "))

while thinkNum != randomNum:
    if thinkNum > randomNum:
        print("Pista: busca un numero menor")
    elif thinkNum < randomNum:
        print("Pista: busca un numero mayor")
    thinkNum = int(input("Ingrese el numero: "))
    print("")

if thinkNum == randomNum:
    print("####################################")
    print(f'   Es correcto, el numero es: {randomNum}')
    print("####################################")
