#função que multiplica os 9 primeiros dígitos de um CPF de forma decrescente de 10 até 2
def multiply_digits(cpf_first_digits, LOCAL_MULTIPLY_VALIDATION, LOCAL_DIGIT_SUM):
    for digit in cpf_first_digits:
        results = int(digit)*LOCAL_MULTIPLY_VALIDATION
        LOCAL_MULTIPLY_VALIDATION -= 1
        LOCAL_DIGIT_SUM += results
    return LOCAL_DIGIT_SUM

user_cpf = '11144477735'

#Teste para descobrir o penúltimo dígito do CPF do usuário
cpf_first_9_digits = user_cpf[:9]

#constantes para validação do penúltimo número do CPF
MULTIPLY_VALIDATION_1 = 10
CPF_DIGIT_SUM_1 = 0

#função que multiplica os 9 primeiros dígitos de um CPF de forma decrescente de 10 até 2
validated_nine_digits= multiply_digits(cpf_first_9_digits, MULTIPLY_VALIDATION_1, CPF_DIGIT_SUM_1)

division_rest = validated_nine_digits%11

#Validação do penúltimo dígito do CPF do usuário
if division_rest < 2:
    validated_cpf_number = 0
else:
    digit_verify = 11
    digit_result = digit_verify - division_rest
    validated_cpf_number = digit_result

print(user_cpf)
print(validated_cpf_number)