def filtrar(texto, denylist):
    palavras = []
    palavra = ''
    for char in texto:
        if char == ' ':
            palavras.append(palavra)
            palavra = ''
        else:
            palavra += char
    palavras.append(palavra)

    denylist = [palavra.lower() for palavra in denylist]
    texto_filtrado = ' '.join('*' * len(palavra) if palavra.lower() in denylist else palavra for palavra in palavras)
    return texto_filtrado


def main():
  texto = input("Digite o texto: ")
  denylist = input("Digite a lista de palavras proibidas, separadas por espaço: ").split()
  print(filtrar(texto, denylist))

main()
