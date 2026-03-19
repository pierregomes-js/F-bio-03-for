
def main():
    n = int(input('Digite a quantidade de elementos da lista: '))


    lista = []


    for i in range(1, n+1):

        elemento = float(input(f'Elemento {i}: '))

        lista.append(elemento)

    def maior(lista):
        maior = lista[0]

        for i in lista:
            if i > maior:
                maior = i

        return maior
    

    print(f'Maior elemento da lista: {maior(lista)}.')
    
    
    

main()