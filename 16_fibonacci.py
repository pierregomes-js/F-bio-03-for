def main():
    print('__Sequência de Fibonacci__')

    n = int(input('N primeiros termos da sequência: '))

    print(fibonnaci(n))

def fibonnaci(n):
    sequencia = ''
    a = 0
    b = 1

    for i in range(n):
        if i == 0:
            sequencia = str(a)
        else:
            sequencia = sequencia + ', ' + str(a)
            proximo = a + b
            a = b
            b = proximo

    return sequencia





main()