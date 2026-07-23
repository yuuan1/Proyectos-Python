
#   -Escribe una función que reciba dos palabras (String) y retorne
#   verdadero o falso (Bool) según sean o no anagramas.
#   -Un Anagrama consiste en formar una palabra reordenando TODAS
#   las letras de otra palabra inicial.
#   -NO hace falta comprobar que ambas palabras existan.
#   -Dos palabras exactamente iguales no son anagrama.


ASCII_inicial = 0
ASCII_anagramtico = 0
palabra_anagramatica = ""
palabra_inicial = ""



while True:
    palabra_inicial = input("Introdusca la palabra base: ")
    
    if palabra_inicial.isalpha():
        break
    else:
        print("[ValueError] Por favor, introdusca unicamente una palabra")


while True:
    palabra_anagramatica = input("Introdusca la palabra a comparar: ")
    
    if palabra_anagramatica.isalpha():
        break
    else:
        print("[ValueError] Por favor, introdusca unicamente una palabra")



for letra in palabra_inicial:
    letra = ord(letra.lower())
    ASCII_inicial +=letra

for letra in palabra_anagramatica:
    letra = ord(letra.lower())
    ASCII_anagramtico += letra

if ASCII_inicial == ASCII_anagramtico:
    print(f"{palabra_inicial.capitalize()} y {palabra_anagramatica.capitalize()} son un anagrama")

else:
    print(f'{palabra_inicial.capitalize()} y {palabra_anagramatica.capitalize()} no son un anagrama')
