import random

begin = int(input("Digite o primeiro número do sorteio: "))
end = int(input("Digite o último número do sorteio: "))

n = random.randint(begin, end)
print("O número sorteado é {}" .format(n))

##print("="*20)
##print("{:^20}" .format("Parabéns ao vencedor!"))
##print("="*20)
