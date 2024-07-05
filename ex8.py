def intercala(s1, s2):
    s3 = ''
    min_len = min(len(s1), len(s2))
    
    for i in range(min_len):
        s3 += s1[i] + s2[i]

    if len(s1) > len(s2):
        s3 += s1[min_len:]
    elif len(s2) > len(s1):
        s3 += s2[min_len:]
    
    print(s3)

def main():
    s1 = input("Digite uma string: ")
    s2 = input("Digite uma outra string: ")
    intercala(s1,s2)

main()
