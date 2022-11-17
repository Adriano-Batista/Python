import random

#header
print("="*40)
print("{:^40}" .format("Adivinhação Numerada"))
print("="*40)
print("{:^40}" .format("Adivinhe qual o número, de 0 a 10\n"))

#escolha do jogador
resposta = str(input("Deseja jogar [S/N]? ")) .upper() .split()[0]

#tratamento de erro
while resposta not in "SN":
    print("RESPOSTA INVÁLIDA!")
    resposta = str(input("Deseja jogar [S/N]? ")) .upper() .split()[0]


numero = random.randint(0,11)

print("="*40)
print("{:^40}" .format("PREPARE-SE..."))
print("="*40)

#escolha_do_jogador = int(input("Qual o número que você escolheu? "))
escolha_do_jogador = None
i = 0

while escolha_do_jogador != numero:

    escolha_do_jogador = int(input("Qual o número que você escolheu? "))
    i += 1

    if escolha_do_jogador == numero:
        print(f"Parabéns, você acertou!\n O número correto era: {numero} \n Número de tentativas: [{i}]")

    else:

        print("Resposta errada...\n Tente mais uma vez")
