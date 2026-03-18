def main():
    print('__Sequência de Fibonacci__')

    n = int(input('N primeiros termos da sequência: '))

    print(fibonnaci(n))

def fibonnaci(n):
    sequencia = []

    for i in range(n):
        if i == 1 or i == 0:
            sequencia.append(i)
        else:
            elemento = ((i - 1) + (i - 2))
            sequencia.append(elemento)

    return sequencia





main()