from itertools import filterfalse


def jogar():

    print("**********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("**********************************")

    palavra_secret = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print (letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra: ")
        chute = chute.strip()


        posicao = 0
        for letra in palavra_secret:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            posicao = posicao + 1

        print(letras_acertadas)

    print("---------------------")
    print("Fim do jogo! Agradece")
    print("---------------------")

if (__name__ == "__main__"):
    jogar()