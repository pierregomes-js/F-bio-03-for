
def main():
    print('__Empresa__')

    n = int(input('Insira o número de funcionários da empresa: '))

    for i in range(n):
        codigo = int(input(f'Código do funcionário: '))
        horas = float(input(f'Horas trabalhadas do funcionário {codigo}: '))
        salario = horas * 12
        dependentes = int(input(f'Numero de dependentes do funcionário {codigo}: '))
        salario += (dependentes * 40)
        desconto_inss = salario * 0.085
        desconto_ir = salario * 0.05
        print('')
        print('Ficha')
        print(f'Salário líquido do funcionário {codigo}: \n{salario:.2f}R$')
        print(f'Salario descontado do INSS: \n{desconto_inss:.2f}R$')
        print(f'Salario descontado do IR: \n{desconto_ir:.2f}R$')
        print(f'Desconto total: \n{(salario - (desconto_inss + desconto_ir)):.2f}R$')
        print('')

main()