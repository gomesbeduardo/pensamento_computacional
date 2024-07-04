def trocar_elementos(vet):
    n = len(vet)
    for i in range(n // 2):
        vet[i], vet[n - i - 1] = vet[n - i - 1], vet[i]
    return vet

def main():
    vet = []
    tamanho = int(input("Digite o tamanho do vetor: "))
    for i in range(tamanho):
        n = int(input(f"Digite o {i+1} número: ")) 
        vet.append(n)

    print(trocar_elementos(vet))

main()
