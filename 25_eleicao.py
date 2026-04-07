
def main():
    print('__Eleição Presidencial__')

    n = int(input('Digite a quantidade de eleitores: '))

    def ganhador(a, b, c):
            return a > b and a > c
    
    candidato_1 = 0
    candidato_2 = 0
    candidato_3 = 0
    nulo = 0
    branco = 0

    for i in range(n):
        voto = int(input(f'Voto {i}: '))
            
        if voto == 1:
            candidato_1 += 1
        elif voto == 2:
            candidato_2 += 1
        elif voto == 3:
            candidato_3 += 1
        elif voto == 0:
            branco += 1
        else:
            nulo += 1

        
    print(f'Total de votos para candidato 1: {candidato_1}')
    print(f'Total de votos para candidato 2: {candidato_2}')
    print(f'Total de votos para candidato 3: {candidato_3}')
    print(f'Total de votos em nulo: {nulo}')
    print(f'Total de votos para branco: {branco}')

    if ganhador(candidato_1, candidato_2, candidato_3):
        print('O ganhador é o candidato 1.')
    elif ganhador(candidato_2, candidato_1, candidato_3):
        print('O ganhador é o candidato 1.')
    else:
        print('O ganhador é o candidato 3.')


        
        


main()