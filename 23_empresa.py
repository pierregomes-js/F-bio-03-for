#incompleto

def main():
    print('__Empresa__')

    n = int(input('Número de habitantes da cidade: '))

    soma_salarios = 0
    soma_filhos = 0
    contador_salarios = 0

    for i in range(n):
        salario = float(input(f'{i} Salário: '))
        filhos = int(input(f'{i} Número de filhos: '))

        soma_salarios += salario
        soma_filhos += filhos

        contador = 0

        if salario <= 1000:
            contador += 1

    media_salario = soma_salarios / n
    media_filhos = soma_filhos / n
    percentual = (contador / n) * 100

    print('Resultado: ')
    print(f'Média dos salários: {media_salario:.2f}')
    print(f'Média de filhos por cidadão: {media_filhos:.1f}')
    print(f'Percentual da população que ganha até 1000: {percentual:.2f}')

    

 

main()