import random

#contador de vitórias
wins = 0
resposta = 'S'
while resposta == "S":
    while True:

        #header
        print("="*40)
        print("PAR OU ÍMPAR" .center(40))
        print("="*40)

        #escolha da máquina
        pc_number = random.randint(1,10)

        print("ESCOLHA PAR OU ÍMPAR \n[1] PAR \n[2] ÍMPAR")

        #escolha do usuário
        player_choice = int(input("Faça sua escolha: "))
        while player_choice not in range(1, 3):
            player_choice = int(input("RESPOSTA INVÁLIDA! \nFaça sua escolha: "))    
        player_number = int(input("Digite o seu número: "))

        soma = player_number + pc_number

        #processamento
        print(f"Número do jogador = {player_number} \nNúmero da máquina = {pc_number}")
        print(f"A soma dos números é: {soma}")

        #verificação do vencedor
        if player_choice == 1 and (soma % 2 == 0):
            print("A soma dos valores é PAR!")
            print("Player venceu!")
            wins += 1
        elif player_choice == 2 and (soma % 2 != 0 ):
            print("A soma dos valores é ÍMPAR!")
            print("Player venceu!")
            wins += 1
        else:
            print("Player perdeu...")
            break

    #contador de vitórias 
    print("="*40)
    print(f"CONTAGEM DE VÍTORIAS: {wins}" .center(40))
    print("="*40)

    resposta = str(input("Deseja jogar novamente [S/N]? ")).upper().strip()[0] 
    while resposta not in "SN":
        resposta = str(input("RESPOSTA INVÁLIDA! \nDeseja jogar novamente [S/N]? ")).upper().strip()[0] 

#fim algoritmo
print('__FIM__')

    
