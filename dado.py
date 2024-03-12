import random

def rolar_dado():
    while True:
        lado =  int (input ('lados? '))
        while lado == 0:
            print('escolha outro valor')
            lado =  int (input ('lados? '))
        resultado = random.randint(1, lado)
        print("Resultado:", resultado)
        break

rolar_dado()
bis = input('Mais um? (Y/N)')
while bis == 'Y':
    rolar_dado()
    bis = input('Mais um? (Y/N)')
    if bis == 'N':
        print ('Vai embora então')
        break
if bis != 'Y':
    print ('Vai embora então')
