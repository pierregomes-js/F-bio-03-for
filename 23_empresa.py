
def main():
    print('__Empresa__')

    n = int(input('Insira o número de funcionários da empresa: '))

    lista_salario = []
    lista_inss = []
    lista_ir = []

    for i in range(n):
        salario = float(input(f'Horas trabalhadas do funcionário {i}: '))
        salario *= 12
        dependentes = int(input(f'Numero de dependentes do funcionário {i}: '))
        salario += (dependentes * 40)
        desconto_inss = salario * 0.085
        desconto_ir = salario * 0.05
        salario = salario - (desconto_inss + desconto_ir)
        lista_salario.append(salario)
        lista_ir.append(desconto_ir)
        lista_inss.append(desconto_inss)

    print('Ficha')

    print('Listas dos salários líquidos de cada funcionário:')
    numeracao = 0
    for i in lista_salario:
        print(f'Número do funcionário : {numeracao}, salário: {i:.2f}.')
        numeracao += 1

    print('')
    print('Listas do imposto do INSS no salário de cada funcionário:')
    numeracao = 0
    for i in lista_inss:
        print(f'Número do funcionário : {numeracao}, desconto: {i:.2f}')
        numeracao += 1
        
    print('')
    print('Listas do imposto do IR no salário de cada funcionário:')
    numeracao = 0
    for i in lista_ir:
        print(f'Número do funcionário : {numeracao}, desconto: {i:.2f}')
        numeracao += 1



main()