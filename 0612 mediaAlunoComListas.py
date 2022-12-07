'''Escreva um programa que leia nome e média de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela'''
p = 40
schoolClass = list()
students = dict()

def header(headerText):
    print("="*p)
    print(f"{headerText}" .center(p))
    print('='*p)




header('ESCOLA SENAC')

numberOfStudents = int(input('Digite quantos alunos estão na turma: '))

for student in range(0,numberOfStudents):
    print('='*p)
    students['NOME DO ALUNO'] = str(input('Digite o nome do aluno(a): '))
    students['NOTA 1'] = float(input('Digite a primeira nota do aluno: '))
    students['NOTA 2'] = float(input('Digite a segunda nota do aluno: '))
    averageGrade = (students['NOTA 1'] + students['NOTA 2'])/2
    students['MÉDIA'] = averageGrade
    schoolClass.append(students.copy())
    students.clear

header('TURMA')

for students in schoolClass:
    for key, value in students.items():
        print(f"{key} = {value}")
