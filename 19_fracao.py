#incompleto
def main():
    n = int(input('N: '))

    somatorio_par = 0
    somatorio_impar = 0


    for x in range(n, 1, -2):
        numerador_par = x

    for y in range(1, n+1, 2):
        denominador_par = y

    for m in range(1, n+1, 2):
        numerador_impar = m

    for n in range(n, 1, -2):
        denominador_impar = n

    for k in range(1, n+1):
        
        somatorio += numerador / denominador



    print(f'S = {somatorio:.2f}')


main()