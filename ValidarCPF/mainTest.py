#Validador de CPF
#cpf de teste: 11144477735


#Função remove os pontos e traços do CPF digitado pelo usuário
def punctuation_replace(punctuation_user_cpf):
    if '.' in punctuation_user_cpf or '-' in punctuation_user_cpf:
        punctuation_user_cpf = punctuation_user_cpf.replace('.','')
        punctuation_user_cpf = punctuation_user_cpf.replace('-','')
        
    return punctuation_user_cpf


#Função para validar se o CPF do usuário é do tipo numérico E possui 11 dígitos (padrão do CPF)
def numeric_error_treatment(numeric_error_cpf):
    while not numeric_error_cpf.isnumeric() or len(numeric_error_cpf) != 11:
        numeric_error_cpf = (input('Erro! Digite um valor correto: '))
    return numeric_error_cpf


#função que multiplica os 9 primeiros dígitos de um CPF de forma decrescente de 10 até 2
def multiply_digits(cpf_first_digits, LOCAL_MULTIPLY_VALIDATION, LOCAL_DIGIT_SUM):
    for digit in cpf_first_digits:
        results = int(digit)*LOCAL_MULTIPLY_VALIDATION
        LOCAL_MULTIPLY_VALIDATION -= 1
        LOCAL_DIGIT_SUM += results
    return LOCAL_DIGIT_SUM


#-------------------------#
#           MAIN          #
#-------------------------#


while True:
    user_cpf = input('Digite seu CPF: ')
    
    #Remove os pontos e traços do CPF digitado pelo usuário
    user_cpf = punctuation_replace(user_cpf)

    #Teste para validar se o CPF do usuário é do tipo numérico e possui 11 dígitos (padrão do CPF)
    treated_cpf = numeric_error_treatment(user_cpf)

    #Teste para descobrir o penúltimo dígito do CPF do usuário
    cpf_first_9_digits = user_cpf[:9]

    #constantes da validação do penúltimo número do CPF
    MULTIPLY_VALIDATION_1 = 10
    CPF_DIGIT_SUM_1 = 0
    

    #multiplica os 9 primeiros dígitos de um CPF de forma decrescente de 10 até 2
    validated_nine_digits= multiply_digits(cpf_first_9_digits, MULTIPLY_VALIDATION_1, CPF_DIGIT_SUM_1)
    
    division_remainder = validated_nine_digits%11

    #validação do penúltimo dígito do CPF do usuário
    if division_remainder < 2:
        validated_cpf_number = 0
    else:
        digit_verify = 11
        digit_result = digit_verify - division_remainder
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