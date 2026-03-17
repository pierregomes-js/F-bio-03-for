def main():
    n = int(input('Digite a quantidade de elementos da lista: '))


    lista = []


    for i in range(1, n+1):

        elemento = float(input(f'Elemento {i}: '))

        lista.append(elemento)


    def maior(lista, n):
        maior = 0

        for i in range(n):
            if maior > lista[i]:
                maior == lista[i]
                continue
            else:
                continue

        return maior
    

    print(f'Maior elemento da lista: {maior(lista, n)}.')
    
    
    

main()