def header_tabuada():
    print("="*40)
    print("{:^40}" .format("TABUADA DO {}") .format(fator_usuario))
    print("="*40)

def tabuada():
    for i in range (1,10):
        print(f"{fator_usuario} X {i} = {fator_usuario*i}" .center(40))
        

while True:

    fator_usuario = int(input("Digite qual tabuada você deseja ver: "))

    if fator_usuario == 0:
        print("Fim.")
        break
        

    else:
        header_tabuada()

        tabuada()
        print("="*40)     
