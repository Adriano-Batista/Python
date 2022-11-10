nome = input("Escreva o nome do aluno: ")
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

med = (n1+n2)/2

print(" ")
if med >= 70:
    print("Aluno {} aprovado!" .format(nome))
    print("Nota final: {}" .format(med))

    if med == 77:
        print("\033[33mParabéns. Você encontrou o easter egg!\033[m")
        print("O aluno {} foi aprovado!" .format(nome))
        print("Nota final: {}" .format(med))

else:
    print("Aluno {} reprovado." .format(nome))
    print("Nota final: {}" .format(med))

print("Até o ano próximo semestre!")
