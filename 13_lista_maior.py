
def main():
    n = int(input('Digite a quantidade de elementos da lista: '))


    maior_num = 0

    for i in range(n):

        elemento = float(input(f'Elemento {i}: '))

        if elemento > maior_num:
            maior_num = elemento

    print(f'Maior elemento da lista: {maior_num}.')
    
    
    

main()