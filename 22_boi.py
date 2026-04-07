
def main():
    n = int(input('Número de bois: '))
    n_gordo = 0
    mais_gordo = 0

    for i in range(n):
        kg = int(input(f'Peso em kg do boi {i}: '))
        codigo = int(input(f'Código do boi {i}: '))
        if i == 0:
            mais_magro = kg
            n_magro = codigo

        if kg > mais_gordo:
            mais_gordo = kg
            n_gordo = codigo

        if kg < mais_magro:
            mais_magro = kg
            n_magro = codigo


    print(f'O boi mais pesado é o de número {n_gordo} e pesa {mais_gordo}kg.')
    print(f'O boi mais leve é o de número {n_magro} e pesa {mais_magro}kg.')


main()