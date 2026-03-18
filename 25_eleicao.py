
def main():
    print('__Eleição Presidencial__')

    n = int(input('Digite a quantidade de eleitores: '))

    def ganhador(a, b, c):
            return a > b and a > c
    
    candidato_1 = []
    candidato_2 = []
    candidato_3 = []
    nulo = []
    branco = []

    for i in range(1, n+1):
        voto = int(input(f'Voto {i}: '))
            
        if voto == 1:
            candidato_1.append(voto)
        elif voto == 2:
            candidato_2.append(voto)
        elif voto == 3:
            candidato_3.append(voto)
        elif voto == 0:
            branco.append(voto)
        else:
            nulo.append(voto)

        
    print(f'Total de votos para candidato 1: {len(candidato_1)}')
    print(f'Total de votos para candidato 2: {len(candidato_2)}')
    print(f'Total de votos para candidato 3: {len(candidato_3)}')
    print(f'Total de votos em nulo: {len(nulo)}')
    print(f'Total de votos para branco: {len(branco)}')

    if ganhador(candidato_1, candidato_2, candidato_3):
        print('O ganhador é o candidato 1.')
    elif ganhador(candidato_2, candidato_1, candidato_3):
        print('O ganhador é o candidato 1.')
    else:
        print('O ganhador é o candidato 3.')


        
        


main()