#Numero de Armstrong
"""Es aquel numero que es igual a la suma de sus dijitos elevados a la potencia
de la cantidad de digitos que lo conforma"""

numero = input("Introdusca su numero:")
digitos = []

for digito in numero:
    digitos.append(digito)

suma_potencia = 0
expontente = len(digitos)

for digito in digitos:
    digito_entero = int(digito)
    suma_potencia += digito_entero ** expontente

if suma_potencia == int(numero):
    print("Si es un numero Armstrong")
else:
    print("No es un numero Armstrong")
    print(f'Da como resultado {suma_potencia}')
    

