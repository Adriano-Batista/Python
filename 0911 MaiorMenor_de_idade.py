#entrada de dados
nome = input("Escreva seu nome: ")
idade = int(input("Digite sua idade: "))

volte_em = 18 - idade 

#saida de dados
if idade < 18: 
    print ("{}, você é menor de idade. Tem apenas {}. Volte daqui {} anos" .format(nome, idade, volte_em))
else:
    print ("{}, você é maior de idade! Tem {} de idade" .format(nome, idade))

#em apenas 1 linha

#header
print("="*20)
print("{:^20}" .format("APENAS 1 LINHA"))
print("="*20)
#saida de dados
print("{} você é menor de idade. Volte em {} anos" .format(nome, volte_em) if idade < 18 else "{} você é maior de idade!" .format(nome)) 