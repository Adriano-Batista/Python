#Variáveis
res = float

print("="*40)
print("{:^40}" .format("Calculadora de operações básicas"))
print("="*40)

n1 = float (input("Digite o primeiro número: "))
op = input("A operação: ")
n2 = float (input("Digite o segundo número: "))

if op == "+":
    res = n1+n2
    print(res)



if op == "-":
    res = n1-n2
    print(res)

if op == "*":
    res = n1*n2
    print(res)

if op == "/":
    res = n1/n2
    print(res)
