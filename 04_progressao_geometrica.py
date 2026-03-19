
def main():
    print('__Progressão Aritmética__')

    valor_inicial = int(input('Valor inicial: '))
    limite = int(input('Limite: '))
    r = int(input('Razão: '))

    valor = valor_inicial
    #printar valor inicial
    print(valor)

    for i in range(limite):
        valor *= r
        if valor < limite:
            print(valor)
            





main()