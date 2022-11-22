numero = ('zero', 'um','dois','três','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero_escolhido = (int(input("Digite um número de 0 a 10: ")))

while numero_escolhido not in range(0,21):
    print ("Número inválido! \nDigite um valor entre 0 e 20")
    numero_escolhido = (int(input("Digite um número de 0 a 10: ")))

print(f"O número {numero_escolhido} escrito por extenso é: {numero[numero_escolhido]}")


