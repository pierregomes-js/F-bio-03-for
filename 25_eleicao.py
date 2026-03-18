def main():
    print('__Eleição Presidencial__')

    n = int(input('Digite a quantidade de eleitores: '))

    urna_eletronica = urna(n)
    total_candidato_1 = votos_1(urna_eletronica)


    def urna(n):
        votos = []
        for i in range(1, n+1):
            voto = input(f'Voto {i}: ')
            votos.append(voto)
        return votos
    
    def votos_1(urna_eletronica):
        candidato_1 = []
        for i in range(urna_eletronica):
            if urna_eletronica[i] == 1:
                candidato_1 += 1
            else:
                continue

        return len(candidato_1)
            
    urna(n)
    print(urna_eletronica)
    print(total_candidato_1)
    
        


main()