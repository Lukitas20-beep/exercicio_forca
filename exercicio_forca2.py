palavra = "Tabias"
letras = []
chances = 4
ganhar = False
while True:
    for letra in palavra:
        if letra in letras:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("Você tem essas tentativas: ", chances)
    tentativa = input("Digite a letra que você quer tentar colocar: ")
    letras.append(tentativa)
    if tentativa not in palavra:
        chances -= 1
    if chances == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0  ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0  ")
        print("|    |  ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0  ")
        print("|   /|\  ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif chances == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|    0  ")
        print("|   /|\  ")
        print("|    /\  ")
        print("|      ")
        print("_      ")
        print()
    ganhar = True
    for letra in palavra:
        if letra not in letras:
            ganhar = False
    if chances == 0 or ganhar:
        break

if ganhar == True:
    print("Você acertou a palavra era: ",palavra)
else:
    print("Você errou, a palavra era: ",palavra)
