#   -Crea una única función (importante que sólo sea una) que sea capaz
#   de calcular y retornar el área de un polígono.
#   -La función recibirá por parámetro sólo UN polígono a la vez.
#   -Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#   -Imprime el cálculo del área de un polígono de cada tipo. 

triangulo = 0
base = 0
altura = 0

def formulasa():
    while True:
        try:
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            if base <= 0 and altura <= 0:
                print("\033[31mLos valores deben ser mayores a 0\033[0m\n")
                continue
            return base, altura
        except: 
            print(f'\033[31mIngrese solo caracteres numericos\033[0m\n' )   


while True:
    
    try:
        menu = input("Ingrese la opcion deseada:\n"
                     "1) Triangulo\n"
                     "2) Cuadrado\n"
                     "3) Rectangulo\n"
                     "Ingresar:  ")
        
        int(menu)
        print("\nIngrese alguno de las opciones\n") 

    except:
        menu = menu.lower()
                                   
        if menu == "triangulo"  or menu == "cuadrado" or menu == "rectangulo":
            break
        else:
            print("\nIngrese alguno de las opciones\n")

if menu == "triangulo":
    print(f'\nOPCION ELEGIDA: {menu}\n')

    base, altura = formulasa()
    triangulo = (base * altura)/ 2

    print(triangulo)

elif menu == "cuadrado" or menu == "rectangulo":
    print(f'OPCION ELEGIDA: {menu}\n')

    base, altura = formulasa()
    cuadrado_rectangulo = base * altura

    print(f'El area del {menu} es: {cuadrado_rectangulo}')
