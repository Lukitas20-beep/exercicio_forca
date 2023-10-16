palavra = "cavalo"
letras_usuario = []
chances = 7
ganhou = False

while True:
    for letra in palavra:
        if letra in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("Você tem: ", chances, "chances")
    tentativa = input("Digite as letras (minúsculas) para tentar adivinhar a palavra: ")
    letras_usuario.append(tentativa)
    if tentativa not in palavra:
        chances -= 1
    if chances == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0  ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0  ")
        print("|   /   ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0 ")
        print("|   / |  ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0  ")
        print("|   /|\   ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0  ")
        print("|   /|\   ")
        print("|   /  ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0  ")
        print("|   /|\   ")
        print("|   /\  ")
        print("|      ")
        print("_      ")
        print()
    ganhou = True
    for letra in palavra:
        if letra not in letras_usuario:
            ganhou = False
    if chances == 0 or ganhou:
        break

if ganhou:
    print("Você ganhou, a palavra era: ", palavra)
else:
    print("Você perdeu, a palavra era: ", palavra)
