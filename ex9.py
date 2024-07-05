def imprime_gradual(s):
    meio = len(s) // 2
    for i in range(1, meio + 2):
        print(s[meio - i + 1: meio + i])

def main():
    s = input("Digite uma palavra com número ímpar de caracteres: ")
    imprime_gradual(s)

main()
