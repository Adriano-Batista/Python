#enunciado do exercício
'''Escreva um programa que vai gerar cinco números aleatórios e colocar dentro em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
#biblioteca/documentação
import random

#variavel que gera números aleatórios
numeros = random.randint

#output do número
print("Lista dos números: ")
for _ in range(0,5):
    tupla_dos_numeros = (numeros(0,10))
    print(tupla_dos_numeros, end=' ')
print('\n')


'''versão com upgrades'''

extensao_tupla = int((input("Digite o último número da sua lista: ")))
limite_numero_aleatorio = (int(input("Digite o limite do seu número gerado aleatoriamente")))
print("EX: 10 ou seja, serão gerados números de 0 a 10: ")

print("Lista dos números: ")

#output do número
for _ in range(0,extensao_tupla):
    tupla_dos_numeros = (numeros(0,limite_numero_aleatorio))
    print(tupla_dos_numeros, end=' ')