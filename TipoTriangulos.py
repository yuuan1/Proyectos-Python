print("===============================")
print("    QUE TRIANGULO TENGO?")
print("===============================")

while True:
    mensaje = input("Deseas que su triangulo se analice mediante:\n"
                    '1) Su angulos\n'
                    '2) Sus rectas\n'
                    'Ingrese su opcion: ')
    if mensaje in ['1','2']:
        while True:
            if mensaje == '1':
                try:
                    primer_angulo = int(input("Ingrese el primer angulo(solo el numero): "))
                    segundo_angulo = int(input("Ingrese el segundo angulo(solo el numero): "))
                    tercer_angulo = int(input("Ingrese el tercer angulo(solo el numero): "))
                except ValueError:
                    print("[Error] Ingresaste letras o caracteres no válidos. Inténtalo de nuevo.\n")
                    continue
                
                if primer_angulo < 90 and segundo_angulo < 90 and tercer_angulo < 90:
                    print("Tu triangulo es un triangulo Acutángulo")
                elif (90 < primer_angulo < 180) or (90 < segundo_angulo < 180) or (90 < tercer_angulo < 180):
                    print("Tu triangulo es un triangulo Obtuso")
                else: 
                    print("Tu triangulo es un triangulo Rectangulo")
    
                break

            if mensaje == '2':
                try:
                    primer_angulo = int(input("Ingrese la primera recta(solo el numero): "))
                    segundo_angulo = int(input("Ingrese la segunda recta(solo el numero): "))
                    tercer_angulo = int(input("Ingrese la tercera recta(solo el numero): "))
                except ValueError:
                    print("[Error] Ingresaste letras o caracteres no válidos. Inténtalo de nuevo.\n")
                    continue

                if primer_angulo == segundo_angulo == tercer_angulo:
                    print("Tu triangulo es un triangulo Equilátero")
                elif (primer_angulo == segundo_angulo or segundo_angulo == tercer_angulo or primer_angulo == tercer_angulo) and not (primer_angulo == segundo_angulo == tercer_angulo):
                    print("Tu triangulo es un triangulo Isósceles")
                else:
                    print("Tu triangulo es un triangulo Escaleno")
                break
        break

    else:
        print(f"COMO VAS A" 
                f"PONER {mensaje}, QUE TE DIJE...\n")