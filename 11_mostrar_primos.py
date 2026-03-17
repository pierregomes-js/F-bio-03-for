def main():
    

    inferior = int(input('Limite inferior: '))
    superior = int(input('Limite superior: '))
    

    for i in range(inferior, superior+1):
        if eh_primo(i):
            print(i)


def eh_primo(n):

    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == 2 or n == 3 or n == 7:
        return True
    elif n % 2 != 0 and n % 3 != 0 and n % 7 != 0:
        return True
    else:
        return False


main()