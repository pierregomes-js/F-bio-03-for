
def main():
    n = int(input('N: '))

    somatorio_par = 0
    somatorio_impar = 0

    for k in range(1, n+1):
        
        if k % 2 == 0:
            elemento_par = (((n + 1) - k) / k)
            somatorio_par += elemento_par
        else:
            elemento_impar = (k / ((n + 1) - k))
            somatorio_impar += elemento_impar

    print(f'S = {somatorio_impar - somatorio_par}')


main()
