def eh_palindromo(string):
    string_sem_espaco = string.replace(' ', '')
    string_lower = string_sem_espaco.lower()
    string_reversa = string_lower[::-1]
    if string_reversa == string_lower:
        print (f"A string ({string}) é palíndromo")
    else:
        print (f"A string ({string}) não é palíndromo")


def main():
    string = input("Digite uma string: ")
    eh_palindromo(string)

main()
