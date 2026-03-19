def main():
    n = int(input('N: '))

    somatorio = 0
    for i in range(1, n+1):
        numerador = i
    for j in range(n, 1, -1):
        denominador = j

    for k in range(n):
        somatorio += numerador / denominador



    print(f'S = {somatorio:.2f}')


main()