
def main():
    n = int(input('Número de bois: '))


    lista = []

    for i in range(n):
        kg = int(input(f'Peso em kg do boi {i}: '))
        lista.append(kg)

    def mais_pesado(lista):
        mais_pesado = lista[0]

        for i in lista:
            if i > mais_pesado:
                mais_pesado = i

        return mais_pesado
    
    mais_gordo = mais_pesado(lista)
    
    def mais_leve(lista):
        mais_leve = lista[0]

        for i in lista:
            if i < mais_leve:
                mais_leve = i

        return mais_leve
        
    mais_magro = mais_leve(lista)
        
    def numeracao(lista, mais):
        numeracao = 0
        for i in lista:
            if i == mais:
                return numeracao
            else:
                numeracao += 1
        return numeracao
        
    codigo_gordo = numeracao(lista, mais_gordo)
    codigo_magro = numeracao(lista, mais_magro)

    print(f'O boi mais pesado é o de número {codigo_gordo} e pesa {mais_gordo}kg.')
    print(f'O boi mais leve é o de número {codigo_magro} e pesa {mais_magro}kg.')





main()