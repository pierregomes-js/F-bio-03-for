def main():
    n = int(input('Digite um valor N: '))

    menor_quadrado = int((n ** 0.5) - 1) ** 2

    print(f'O menor quadrado é {menor_quadrado}')


main()