#Descobrir se o ano é bissexto ou não

#entrada de dados do usuário
ano = int(input("Digite o ano que deseja descobrir se é bissexto ou não: "))
#se o ano for divisível por 4, continua o teste, se não não é bissexto
if (ano%4==0):
    #se o ano não for divisível por 100 é um ano bissexto, se não continua o teste
    if (ano%100==0):
        #se o ano for divisível por 400 é um ano bissexto, se não ele não é.
        if (ano%400==0):
            print("{} é um ano bissexto!" .format(ano))
        else:
            print("{} não é um ano bissexto." .format(ano))
    else:
        print("{} é um ano bissexto!" .format(ano))
else:
    print("{} Não é um ano bissexto." .format(ano))
    
