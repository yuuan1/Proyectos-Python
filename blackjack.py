import random

print("\033[1;33m==================================")
print("           BLACK JACK")
print("==================================\033[0m")

croupier = 0
user = 0 
cartas = 0
i = 0
ROJO = "\033[1;31m"
RESET = "\033[0m"

opcion_elegida = {
    '\n1': ')Pedir carta(Hit)',
    '2': ')plantarse(Stand)\n'
}

def ramdomicer(es_croupier = False):
    global i
    baraja = [1,2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']
    carta_sacada = random.choice(baraja)

    if type(carta_sacada) == int:
        print(f'Salio la carta {carta_sacada}')
        return carta_sacada
    
    elif type(carta_sacada) == str and carta_sacada != 'A':
        print(f'Salio la carta: {carta_sacada}\nSe suman 10 puntos')
        return 10

    else:
        print("Ha salido la letra A")
        if es_croupier:
            print("Se suma 1 punto al croupier")
            return 1
        
        while True:
            carta = input("Deseas que su valor sea 1 o 11:\n Tu opcion:")
            if carta in ['1','11']:
                return int(carta)
            else:
                print(f"COMO VAS A 
                    PONER {carta}, QUE TE DIJE")
            

def croupier_turno():
    global croupier
    print(f'\n{ROJO}------Turno del croupier------{RESET}\n')
    carta_obtenida = ramdomicer(es_croupier=True) 
    croupier += carta_obtenida
    print(f'Puntos totales: {croupier}\n')
    return croupier
        
def user_turno():
    global user
    print(f'\n{ROJO}------Tu turno------{RESET}\n')
    carta_obtenida = ramdomicer(es_croupier=False)
    user += carta_obtenida
    print(f'Tus puntos totales: {user}')
    return user

croupier_turno()
user_turno()

while user < 21:
    for opcion, numero in opcion_elegida.items():
        print(f'{opcion}{numero}')

    opcion = input("Opción: ")

    if opcion == "1":
        user_turno()
        if user > 21:
            print(f'Te pasaste, perdiste con {user} puntos')
            break
    elif opcion == "2":
        print("Te has plantado.\n")
        break
    else:
        print("\n[ERROR] Ingrese una de las opciones válidas")
    
if user <= 21:
    print("--- El croupier define su jugada ---")
    while croupier < 17:
        croupier_turno()

    print(f'PUNTUACIONES FINALES: \n  TU: {user}\n  CROUPIER: {croupier}')

    if croupier > 21:
        print("El croupier se pasó, ganaste")
    elif user > croupier:
        print("Ganaste por tener más puntos")
    elif user < croupier:
        print("Perdiste por tener menos puntos")
    else:
        print("Empate")