def main():
    print('__Sequência de Fibonacci__')

    n = int(input('N primeiros termos da sequência: '))

    for i in range(n):
        fibonnaci(n, i)

def fibonnaci(n, i):
    sequencia = []

    for i in range(n):
        if i == 1 or i == 0:
            continue
        else:



main()