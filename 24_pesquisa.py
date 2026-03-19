
def main():
    print('__Empresa__')

    n = int(input('Número de habitantes da cidade: '))

    soma_salarios = 0
    soma_filhos = 0
    contador_salarios = 0

    for i in range(n):
        salario = float(input(f'Salário do habitante {i}: '))
        filhos = int(input(f'Número de filhos do habitante {i}: '))

        soma_salarios += salario
        soma_filhos += filhos

        if salario <= 1000:
            contador_salarios += 1

    media_salario = soma_salarios / n
    media_filhos = soma_filhos / n
    percentual = (contador_salarios / n) * 100

    print('Resultado: ')
    print(f'Média dos salários: {media_salario:.2f}')
    print(f'Média de filhos por cidadão: {media_filhos:.1f}')
    print(f'Percentual da população que ganha até 1000: {percentual:.2f}')

    

 

main()