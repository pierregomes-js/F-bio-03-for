def main():
    n = int(input('Digite a quantidade de elementos da lista: '))


    lista = []


    for i in range(1, n+1):

        elemento = float(input(f'Elemento {i}: '))

        lista.append(elemento)


    def somatorio(lista):

        soma = 0

        for i in lista:
            soma += i

        return soma
    
    
    print(f'Soma dos elementos: {somatorio(lista)}')
    print(f'Média dos elementos: {somatorio(lista) / n}')



main()