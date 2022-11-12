#Algoritmo financeiro

nome = input("Digite seu nome: ")
print("Seja muito bem-vindo(a)! {}" .format(nome))

valor_imovel = float(input("Qual o valor do imóvel que deseja financiar? (sem pontos ou vírgulas) R$ "))
salario = float(input("Qual o valor bruto do seu salário? R$ "))
anos = int(input("Em quantos anos você deseja pagar o financiamento? "))

prestacao_mensal = valor_imovel/(anos*12)

if prestacao_mensal <= salario*0.3:
    print("Parabéns! {} seu financiamento foi aprovado" .format(nome))
    print("Sua parcela ficará em R$ {:.2f} durante {} anos" .format(prestacao_mensal, anos))
else:
    print("Financiamento negado.")

