def gerar_intervalo_incrementado(n, i):
    if i <= 0:
        return "O incremento deve ser maior que 0."
    return [x for x in range(0, n+1, i)]

def main():
  n = int(input("Digite o valor de N: "))
  i = int(input("Digite o valor de incremento i: "))
  print(gerar_intervalo_incrementado(n, i))

main()
