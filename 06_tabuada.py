#incompleto

def main():
    print('__Tabuada__')

    print('Tabuada da multiplicação: ')

    for i in range(1, 11):
        print(' ')
        print(f'Tabuada do número {i}: ')
        
        for j in range(0, 11):
            print(f'{i} * {j} = {i * j}')

    valor = int(input('Insira um valor para realiza a tabuada: '))
    operacao = int(input('insira a operação(1: soma, 2: subtração, 3: multiplicação, 4: divisão): '))

    if operacao == 3:
        for i in range(1, 11):
            print(' ')
            print(f'Tabuada do número {valor}: ')
        
            for j in range(0, 11):
                print(f'{valor} * {j} = {valor * j}')

            


main()