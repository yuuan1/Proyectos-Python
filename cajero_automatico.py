import time

deposito = 0
opcion = 0
saldo = 100

def menu():
    while True:
        global opcion
        print("\033[36m\n    MENU DE OPCIONES\n\33[0m")
        print(
            '1) Consultar saldo actual\n'
            '2) Depositar dinero\n'
            '3) Retirar dinero\n'
            '4) Salir del sistema\n'
             )
    
        opcion = input("Ingrese la opcion elegida: ")
        try:
            opcion = int(opcion)
            if opcion >= 1 and opcion <= 4:
                return opcion
            else:
               print("\n\033[31m [ERROR]Introduzca una opcion valida")
        except:
            print("\n\033[31m [ERROR]Introduzca una opcion valida")

menu()

while True:
    
    if opcion == 1:
        print(f'\nEl saldo actual es de: \033[32m${saldo}\033[0m')
        time.sleep(2.5)
        menu()
    elif opcion == 2:
        try:
            deposito = int(input("Introduzca la cantidad a depositar: \033[32m$"))
            if deposito > 0:
                saldo += deposito
            else:
               print("\033[32m[ERROR]Introdusca un calor mayor a 0")
            
            time.sleep(2.5)
            menu()
        except:
         print("\033[32m[ERROR]Introduzca unicamente el valor a depositar")
    elif opcion == 3:
        try:
          saldo -= int(input("Introduzca saldo a retirar: \033[32m$"))
          time.sleep(2.5)
          menu()
        except:
           print("\033[31m[ERROR] INTRODUZCA EL VALOR A RETIRAR\033[0m)")
    else:
       print("\n\033[31mCERRANDO SESION\033[0m")
       time.sleep(2.5)
       break
