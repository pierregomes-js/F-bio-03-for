def main():
    n = int(input("N: "))
    
    def calculo(n):
        lista = []
        for i in range(1, n+1):
            elemento = 1/i
            lista.append(elemento)
            
        somatorio = 0
        for i in lista:
            somatorio += i
            
        return somatorio
    print(calculo(n))
    
main()