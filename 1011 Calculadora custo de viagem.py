distancia = int(input("Digite a distância percorrida (em KM): "))
if distancia <= 200:
    print("O custo da sua viagem foi: R$ {:.2f}" .format(distancia*0.50))
else:
    print("O custo da sua viagem foi: R$ {:.2f}" .format(distancia*0.45))
