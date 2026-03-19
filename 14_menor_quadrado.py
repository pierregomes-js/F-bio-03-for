
def main():
    n = int(input('Digite um valor N: '))
    
    for i in range(n, 0, -1):
        if (i ** 0.5) % 1 == 0:
            print(f'O maior quadrado próximo de {n} é {i}.')
            break




main()