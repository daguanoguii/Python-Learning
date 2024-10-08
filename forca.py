import random


def jogar():

    hub()

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secret = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secret]

    enforcou = False
    acertou = False
    erro = 0

    print (letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra: ")
        chute = chute.strip()

        if(chute.upper() in palavra_secret.upper()):
            posicao = 0
            for letra in palavra_secret:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[posicao] = letra
                posicao = posicao + 1
        else:
            erro += 1

        enforcou = erro == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você acertou. Parabéns!")
        print(palavra_secret)
    else:
        print("Que pena. Você perdeu!")
        print("A palavra era: {}". format(palavra_secret))
    print("---------------------")
    print("Fim do jogo! Agradece")
    print("---------------------")

if (__name__ == "__main__"):
    jogar()


    def hub():
        print("**********************************")
        print("***Bem vindo ao jogo de Forca!***")
        print("**********************************")