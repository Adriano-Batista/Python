#Validador de CPF
while True:
    user_cpf = input('Digite seu CPF: ')
    
    #Remove os pontos e traços do CPF digitado pelo usuário
    if '.' in user_cpf or '-' in user_cpf:
        user_cpf = user_cpf.replace('.','')
        user_cpf = user_cpf.replace('-','')

    #Teste para validar se o CPF do usuário é do tipo numérico e possui 11 dígitos (padrão do CPF)
    while not user_cpf.isnumeric() or len(user_cpf) != 11:
        user_cpf = (input('Erro! Digite um valor correto: '))

    #Teste para descobrir o penúltimo dígito do CPF do usuário
    cpf_first_9_digits = user_cpf[:9]

    #constantes da validação do penúltimo número do CPF
    MULTIPLY_VALIDATION_1 = 10
    CPF_DIGIT_SUM_1 = 0
    

    #função que multiplica os 9 primeiros dígitos de um CPF de forma decrescente de 10 até 2
    for cpf_digit in cpf_first_9_digits:
        results = int(cpf_digit)*MULTIPLY_VALIDATION_1
        MULTIPLY_VALIDATION_1 -= 1
        CPF_DIGIT_SUM_1 += results
    
    division_rest = CPF_DIGIT_SUM_1%11

    #Validação do penúltimo dígito do CPF do usuário
    if division_rest < 2:
        validated_cpf_number = 0
    else:
        digit_verify = 11
        digit_result = digit_verify - division_rest
        validated_cpf_number = digit_result

    #constantes da validação do último número do CPF
    MULTIPLY_VALIDATION_2 = 11
    CPF_DIGIT_SUM_2 = 0
    
    cpf_first_10_digits = cpf_first_9_digits + str(validated_cpf_number)
    #função que multiplica os 9 primeiros dígitos de um CPF de forma decrescente de 10 até 2
    for cpf_digit in cpf_first_10_digits:
        results = int(cpf_digit)*MULTIPLY_VALIDATION_2
        MULTIPLY_VALIDATION_2 -= 1
        CPF_DIGIT_SUM_2 += results
    
    division_rest_2 = CPF_DIGIT_SUM_2%11

    #Validação do último dígito do CPF do usuário
    if division_rest_2 < 2:
        validated_second_cpf_number = 0
    else:
        second_digit_verify = 11
        second_digit_result = second_digit_verify - division_rest_2
        validated_second_cpf_number = second_digit_result

    validated_cpf = user_cpf[:9] + str(validated_cpf_number) + str(validated_second_cpf_number)
    
    if validated_cpf == user_cpf:
        print('CPF VÁLIDO.')
    else:
        print('CPF INVÁLIDO.')
    break
print(validated_cpf)
