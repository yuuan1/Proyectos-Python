#Generador de contraseñas seguras
import random

letras = ""
letrasmayus = ""
caracteres = ""
numeros = ""
contraseña = ""
listLetras = 'abcdefghijklmnopqrstuvwxyz'
mayusLet = listLetras.upper()
simbolos = list('!°"#$%&/()=?¿¡+}{,.-_:;][*|')

print("==================================")
print("     Generador de contraseñas")
print("==================================")
print("")

cantNum = int(input("Numero de numeros en la pass: "))
cantLet = int(input("Numero de letras en la pass: "))
cantCarac = int(input("Numero de caracteres en la pass:"))
while True:
    largPass = int(input("Largo de la pass: "))
    if largPass >= 20 <= 40:
        break
    else:
        print("Tu contraseña tiene q ser mayor a 20 y menor a 40")
        print("Intente de nuevo \n")


for i in range(cantNum):
    numeros += str(random.randrange(0,9))

for i in range(cantLet):
    letras += str(random.choice(listLetras))
    letrasmayus += str(random.choice(mayusLet))


for i in range(cantCarac):
    caracteres += random.choice(simbolos)


betapass = str(numeros) + letras + caracteres + letrasmayus
contraseña = "".join(random.choice(betapass) for _ in range(largPass))

print("====================================")
print(f'  Tu contraseña es: {contraseña}')
print("====================================")
