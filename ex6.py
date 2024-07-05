def bubble_sort(values, reverse=False):
    n = len(values)
    for i in range(n):
        for j in range(0, n-i-1):
            if (reverse and values[j] < values[j+1]) or (not reverse and values[j] > values[j+1]):
                values[j], values[j+1] = values[j+1], values[j]
    return values


def binary_search(values, target):
    values = bubble_sort(values)
    low, high = 0, len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        elif values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    values = [int(x) for x in input("Digite uma lista de números: ")]
    reverse = input("Digite 'True' para ordenar decrescentemente ou 'False' para ordenar crescentemente: ") == 'True'
    print(bubble_sort(values, reverse))

    target = int(input("Digite o valor a ser buscado: "))
    print(binary_search(values, target))

main()
