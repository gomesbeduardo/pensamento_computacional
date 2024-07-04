def obter_numeros_paridade(n, c):
    if c == 'p':
        return [i for i in range(1, n) if i % 2 == 0]
    else:
        return [i for i in range(1, n) if i % 2 != 0]

def main():
    n = int(input("Digite o valor de N: "))
    c = input("Digite 'p' para pares ou 'i' para ímpares: ")
    print(obter_numeros_paridade(n, c))

main()
