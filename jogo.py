import random

tabuleiro = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

def jogar():
    p = input("Qual possição vc quer jogar?")
    match p:
        case "a1":
            if tabuleiro[0] == "-":
                tabuleiro[0] = "X"
            else:
                print("posição errada, tente de novo")
                jogar()

        case "a2":
            if tabuleiro[1] == "-":
                tabuleiro[1] = "X"
            else:
                print("posição errada, tente de novo")
                jogar()

        case "a3":
            if tabuleiro[2] == "-":
                tabuleiro[2] = "X"
            else:
                print("posição errada, tente de novo")
                jogar()

        case "b1":
            if tabuleiro[3] == "-":
                tabuleiro[3] = "X"
            else:
                print("posição errada, tente de novo")
                jogar()

        case "b2":
            if tabuleiro[4] == "-":
                tabuleiro[4] = "X"
            else:
                print("posição errada, tente de novo")
                jogar()

        case "b3":
            if tabuleiro[5] == "-":
                tabuleiro[5] = "X"
            else:
                print("posição errada, tente de novo")
                jogar()

        case "c1":
            if tabuleiro[6] == "-":
                tabuleiro[6] = "X"
            else:
                print("posição errada, tente de novo")
                jogar()

        case "c2":
            if tabuleiro[7] == "-":
                tabuleiro[7] = "X"
            else:
                print("posição errada, tente de novo")
                jogar()

        case "c3":
            if tabuleiro[8] == "-":
                tabuleiro[8] = "X"
            else:
                print("posição errada, tente de novo")
                jogar()

        case _:
            print("posição inválida, tente novamente")
            jogar()

def maquina_jogar():
    p = random.randint(0, 8)

    while tabuleiro[p] != "-":
        p = random.randint(0, 8)

    tabuleiro[p] = "O"

def verificar_vitoria():
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == "X":
        print("jogador ganhou!")
        return True

    elif tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == "O":
        print("maquina ganhou!")
        return True

    elif tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == "X":
        print("jogador ganhou!")
        return True

    elif tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == "O":
        print("maquina ganhou!")
        return True

    elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == "X":
        print("jogador ganhou!")
        return True

    elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == "O":
        print("maquina ganhou!")
        return True


    # Colunas
    elif tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == "X":
        print("jogador ganhou!")
        return True

    elif tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == "O":
        print("maquina ganhou!")
        return True

    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == "X":
        print("jogador ganhou!")
        return True

    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == "O":
        print("maquina ganhou!")
        return True

    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == "X":
        print("jogador ganhou!")
        return True

    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == "O":
        print("maquina ganhou!")
        return True


    # Diagonais
    elif tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == "X":
        print("jogador ganhou!")
        return True

    elif tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == "O":
        print("maquina ganhou!")
        return True

    elif tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == "X":
        print("jogador ganhou!")
        return True

    elif tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == "O":
        print("maquina ganhou!")
        return True

    return False

def verificar_empate():
    if "-" not in tabuleiro:
        print("Empate!")
        return True

    return False

def mostrar_tabuleiro():
    print("    1     2     3")
    print("--------------------")
    print(f"a |   {tabuleiro[0]}  |  {tabuleiro[1]}  | {tabuleiro[2]}")
    print("--------------------")
    print(f"b |   {tabuleiro[3]}  |  {tabuleiro[4]}  | {tabuleiro[5]}")
    print("--------------------")
    print(f"c |   {tabuleiro[6]}  |  {tabuleiro[7]}  | {tabuleiro[8]}")
    print("\t")
i = 0
while i < 9:
    jogar()
    mostrar_tabuleiro()
    if verificar_vitoria():
        break

    if verificar_empate():
        break

    maquina_jogar()
    mostrar_tabuleiro()
    if verificar_vitoria():
        break
    
    if verificar_empate():
        break

    i += 1
