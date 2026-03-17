def main():
    print('__Múltiplos de N__')


    N = int(input('Insira um valor N: '))
    inferior = int(input('Limite inferior: '))
    superior = int(input('Limite superior: '))
    
    for i in range(inferior, superior+1):
        if i % N == 0:
            print(i)


main()