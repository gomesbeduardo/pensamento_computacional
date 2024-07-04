def tem_caracteristica(num):
    parte1 = num // 100
    parte2 = num % 100
    return (parte1 + parte2) ** 2 == num

def main(): 
    numeros = []
    for i in range(4):
        n = int(input("Digite um número: "))
        numeros.append(n)
    numeros_filtrados = [num for num in numeros if tem_caracteristica(num)]
    print(numeros_filtrados) 

main()
