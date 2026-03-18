def main():
    print('__Pesquisa Municipal__')

    n = int(input('Número de habitantes da cidade: '))

    # salario(n)

    coleta_salario = salario(n)
    # coleta_filhos = filhos(n)
    # percentual_salario = percentual(n)

def salario(n):
    salarios = []

    for i in range(1, n+1):
        salario = float(input(f'Digite o salário do {i} habitante: '))
        salarios.append(salario)


    return salarios


main()