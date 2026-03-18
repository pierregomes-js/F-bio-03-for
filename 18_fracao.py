def main():
    n = int(input("N: "))
    
    def calculo(n):
        lista = []
        for i in range(1, n+1):
            for j in range(n+1, 1, -1):
                elemento = i/j
                lista.append(elemento)
            
        somatorio = 0
        for i in lista:
            somatorio += i
            
        return somatorio
    print(calculo(n))
    
main()