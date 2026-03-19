#incompleto
def main():
    n = int(input('N: '))

    somatorio_par = 0
    somatorio_impar = 0


    for i in range(n, 0, -1):
        decrescente = i

    for j in range(1, n+1):
        crescente = j

    for k in range(1, n+1):
        print(k)
        if k % 2 == 0:
            somatorio_par += (decrescente / crescente)
            print(somatorio_par)
        else:
            somatorio_impar -= (crescente / decrescente)
            print(somatorio_impar)



    


    # somatorio_par = 0
    # somatorio_impar = 0


    # for x in range(n, 1, -2):
    #     numerador_par = x

    # for y in range(1, n+1, 2):
    #     denominador_par = y

    # for m in range(1, n+1, 2):
    #     numerador_impar = m

    # for n in range(n, 1, -2):
    #     denominador_impar = n

    # for k in range(1, n+1):
        
    #     somatorio += numerador / denominador



    # print(f'S = {somatorio:.2f}')
    print(f'S = {somatorio_impar - somatorio_par}')


main()
