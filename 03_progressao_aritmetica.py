def main():
    print('__Progressão Aritmética__')

    valor_inicial = int(input('Valor inicial: '))
    limite = int(input('Limite: '))
    r = int(input('Razão: '))

    for i in range(valor_inicial):
        
        resultado = (valor_inicial + ((i - 1) * r))
        if not maior_que_limite(resultado, limite):
            print(resultado)

def maior_que_limite(valor, limite):
    return valor > limite




main()