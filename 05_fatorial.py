def main():
    print('__Fatorial de um número__')

    n = int(input('Digite um número: '))

    def fatorial(j):
        fatorial = 1

        for i in range(1, j+1):
            fatorial = fatorial * i

        return fatorial
    
    print(f'O fatorial de {n} é {fatorial(n)}.')


main()