import random

def jogar():

    print("**********************************")
    print("Bem vindo ao jogo d *-e Adivinhação!")
    print("**********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tent = 0
    pontos = 1000

    print("Qual nível de dificuldade você deseja escolher:")
    print("[1] Fácil  [2] Médio  [3] Difícil")

    nivel = int(input("Defina o nível: "))
    if (nivel == 1):
        total_de_tent = 15
    elif (nivel == 2):
        total_de_tent = 10
    else:
        if (nivel == 3):
            total_de_tent = 5


    for x in range(1, total_de_tent + 1):
        print("Tentativa {} de {}".format(x, total_de_tent))
        chute_str = input("Digite o seu número de 1 a 100: ")
        print("Você digitou o numero: " , chute_str)
        chute   = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 a 100")
            continue

        acertou = numero_secreto == chute
        menor   = chute > numero_secreto
        x       = x + 1

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(menor):
                print("Passou um pouco, era um valor menor")
            else:
                print("Que pena, era um valor maior")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = (pontos - pontos_perdidos)



    print("---------------------")
    print("Fim do jogo! Agradece")
    print("---------------------")
if (__name__ == "__main__"):
    jogar()