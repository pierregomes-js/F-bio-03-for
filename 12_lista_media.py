def main():
    n = int(input('Digite a quantidade de elementos da lista: '))
    somatorio = 0

    for i in range(n):

        elemento = float(input(f'Elemento {i}: '))

        somatorio += elemento

    media = somatorio / n


    
    
    
    print(f'Soma dos elementos: {somatorio:.2f}')
    print(f'Média dos elementos: {media:.2f}')



main()