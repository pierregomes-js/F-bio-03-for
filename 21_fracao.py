def main():

    somatorio = 0
    for i in range(1, 100, 2):
        numerador = i
        print(numerador)
    for j in range(1, 51):
        denominador = j
        print(denominador)

    for k in range(50):
        somatorio += (numerador / denominador)
        print(somatorio)



    print(f'S = {somatorio:.2f}')


main()