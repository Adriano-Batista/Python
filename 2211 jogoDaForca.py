'''Crie um programa na aula capaz de permitir que o usuário jogue jogo da forca.
O programa deve ter uma escolha de palavras em uma lista ou apenas 1 palavra;
O usuário pode errar apenas 6 vezes, após isso é game over
Obs: Não é permitido o uso de listas ao menos que para a escolha das palavras!'''
from random import choice

palavras = ('ABACAXI', 'MANDIOCA', 'JIBOIA', 'VIAGEM', 'GREENWICH', 'MARAVILHOSA', 'MARTE')

palavraEscolhida = choice(palavras)

p = 40
print("="*p)
print(f"{'JOGO DA FORCA':^40}")
print(f"{'SEJA BEM-VINDO':^40}")
print("="*p)

lerRegras = str(input("Deseja ler as regras? [S/N] ")).upper().strip()[0]

while lerRegras not in "SN":
    print("Resposta inválida!")
    lerRegras = str(input("Deseja ler as regras? [S/N] ")).upper().strip()[0]

if lerRegras == "S":
    print("Você tem 6 chances para acertar a palavra \nPara cada erro seu contador de erros subirá, chegando em 6 você perde. \n")

print("="*p)
print(f"{'VAMOS JOGAR!':^40}")
print("="*p)

erros = 0

#game
while True:
    print(f"\nA palavra escolhida possui {len(palavraEscolhida)} letras")

    for letra in palavraEscolhida:
        print("_", end=" ")

    escolhaLetra = str(input("\nQual letra tem nesta palavra? ")).upper()

  for letra in palavraEscolhida:
        if letra in escolhaLetra:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    if escolhaLetra not in palavraEscolhida:
        erros += 1
        print(f"Você errou!\nErros = {erros}")
