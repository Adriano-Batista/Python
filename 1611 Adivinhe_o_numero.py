import random

#header
print("="*40)
print("{:^40}" .format("Adivinhação Numerada"))
print("="*40)
print("{:^40}" .format("Adivinhe qual o número, de 0 a 10\n"))

numero = random.randint(0,10)
resposta = 0

def game():
    escolha_do_jogador = None
    i = 0
    while escolha_do_jogador != numero:

        escolha_do_jogador = int(input("Qual o número que você escolheu? "))
        while escolha_do_jogador < 0 or escolha_do_jogador > 10:
            print("RESPOSTA INVÁLIDA!")
            escolha_do_jogador = int(input("Qual o número que você escolheu? "))
        i += 1

        if escolha_do_jogador == numero:
            print(f"Parabéns, você acertou!\n O número correto era: {numero} \n Número de tentativas: [{i}]")

        else:
            print("Resposta errada...\n Tente mais uma vez")

#escolha do jogador
resposta = str(input("Deseja jogar [S/N]? ")) .upper() .split()[0]

#tratamento de erro
while resposta not in "SN":
    print("RESPOSTA INVÁLIDA!")
    resposta = str(input("Deseja jogar [S/N]? ")) .upper() .split()[0]

while resposta == "S":
    #quantidade de jogadores
    quantidadeJogadores = int(input("Quantos jogadores desejam jogar? "))

    for i in range(quantidadeJogadores):
        i+=1
        print("="*40)
        print("{:^40}" .format(f"JOGADOR {i} PREPARE-SE..."))
        print("="*40)

        game()

    resposta = str(input("Deseja jogar [S/N]? ")) .upper() .split()[0]

    if resposta == "N": 
        print("="*40)
        print("{:^40}" .format("FIM DE JOGO"))
        print("="*40)
        break
