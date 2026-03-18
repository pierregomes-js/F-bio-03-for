def main():
    n = int(input("N: "))
    
    def calculo(n):
        
            
        somatorio = 0

        
        for i in range(1, n+1):
            elemento = 1/i
            if i % 2 == 0:
                somatorio -= elemento
            else:
                somatorio += elemento
            
        return somatorio
    print(calculo(n))
    
main()