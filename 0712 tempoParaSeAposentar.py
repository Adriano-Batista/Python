'''Escreva um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário se por acaso a CTPS (Carteira de Trabalho e Previdência Social) for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar. (Considere 35 anos de colaboração para se aposentar)'''
import datetime
from operator import truediv

citizens = dict()

todayYear = datetime.datetime.now()
timesItPrints = 80
printedDots = 30

def headLine(textInTheMiddle):
    print(f"{'='*timesItPrints}")
    print(f"{textInTheMiddle.center(timesItPrints)}")
    print(f"{'='*timesItPrints}")

headLine('CALCULADORA PREVIDENCIÁRIA')

print(f"{'SEJA BEM-VINDO'.center(timesItPrints)}")

print('='*timesItPrints)



while True:
    citizenName = input('Digite seu nome(a): ')
    while not citizenName.isalpha():
        citizenName = input('\033[31mErro\033[m! \nDigite seu nome(a): ')
    citizenName = str(citizenName.capitalize())
    citizens['Nome'] = citizenName

    birthYear = input('Digite seu ano de nascimento: ')
    while not birthYear.isnumeric() or len(birthYear) != 4:
        birthYear = input("\033[31mErro\033[m! \nDigite um valor correspondente a sua idade [YYYY]: ")
    birthYear= int(birthYear)
    age = todayYear.year - birthYear
    citizens['Idade'] = age


    if age < 18:
        headLine('É preciso por lei ser maior de idade para trabalhar.')
        break
    else:

        age = todayYear.year - birthYear
        citizens['Idade'] = age

        ctps = input('Digite os 8 dígitos de sua CTPS: ')
        while not ctps.isnumeric() or len(ctps) != 8:
            ctps = input("\033[31mErro\033[m! \nDigite os 8 dígitos contidos em sua CTPS: ")
        ctps = int(ctps)
        citizens['Carteira de Trabalho'] = ctps

        yearHired = input('Digite o ano de contratação: ')
        while not yearHired.isnumeric() or len(yearHired) != 4:
            yearHired = input("\033[31mErro\033[m! \nDigite o ano de contratação [YYYY]: ")
        yearHired= int(yearHired)
        citizens['Ano de Contratação'] = yearHired

        retireYear = yearHired + 35
        citizens['Ano de Aposentadoria'] = retireYear



        retireAge = 35 - (todayYear.year - yearHired)
        citizens['Idade de Aposentadoria'] = retireAge

        if citizens['Idade de Aposentadoria'] > 35:
            citizens['Direito a aposentadoria'] = 'Possui direito'
        else:
            citizens['Direito a aposentadoria'] = 'Não possui direito'

        print('='*timesItPrints)

        for key, value in citizens.items():
            print(f"{key} {'.'*printedDots} {value}")

        print('\nObrigado por utilizar a calculadora')
        break
    