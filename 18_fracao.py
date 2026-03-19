def main():
    n = int(input('N: '))

    somatorio = 0

    for k in range(n):
        somatorio += k / ((n+1) -k )



    print(f'S = {somatorio:.2f}')


main()