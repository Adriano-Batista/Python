'''Crie um programa na aula capaz de permitir que o usuário jogue jogo da forca.
O programa deve ter uma escolha de palavras em uma lista ou apenas 1 palavra;
O usuário pode errar apenas 6 vezes, após isso é game over
Obs: Não é permitido o uso de listas ao menos que para a escolha das palavras!'''

from dataclasses import replace

palavraEscolhida = str("abacaxi").upper() .strip()

print("="*40)
print("{:^40}" .format("JOGO DA FORCA"))
print("{:^40}" .format("SEJA BEM-VINDO"))
print("="*40)

lerRegras = str(input("Deseja ler as regras? ")) .upper().strip()[0]

while lerRegras not in ("SN"):
    print("Resposta inválida!")
    lerRegras = str(input("Deseja ler as regras? ")) .upper().strip()[0]


if lerRegras == "S":
    print("Você tem 6 chances para acertar a palavra \nPara cada erro seu contador de erros subirá, chegando em 6 você perde. \n")

print("="*40)
print("{:^40}" .format("VAMOS JOGAR!"))
print("="*40)

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
    
    
    
    
    
    
    
    
    #Códigos perdidos no limbo pra excluir depois
    
    '''print(f"A palavra escolhida possui {len(palavraEscolhida)} letras")
    palavraEscolhidaAlterada = (palavraEscolhida.replace(palavraEscolhida, "_ "*7))
    print(palavraEscolhidaAlterada)
    #print(palavraEscolhida.replace(palavraEscolhida, "_", len(palavraEscolhida)))'''

    '''if escolhaLetra in palavraEscolhida:
        escolhaLetra.replace(palavraEscolhidaAlterada, escolhaLetra)
        print(escolhaLetra)'''

    '''palavraEscolhida.find(escolhaLetra)
    if palavraEscolhida.find != -1:
        palavraEscolhida.split()[0:8]
        print(palavraEscolhida.replace(palavraEscolhidaAlterada, escolhaLetra))
        #print(palavraEscolhida.replace(palavraEscolhidaAlterada, escolhaLetra))'''



#.upper().split()[0:8]
