def main():
    
    def calculo():
        lista = []
        for i in range(1, 100, 2):
            for j in range(1, 51):
                elemento = i/j
                lista.append(elemento)
            
        somatorio = 0
        for i in lista:
            somatorio += i
            
        return somatorio
    print(calculo())
    
main()