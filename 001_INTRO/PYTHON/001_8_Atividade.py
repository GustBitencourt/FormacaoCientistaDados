def amplitude(arr):
    return len(arr)


amplitude([1, 2, 3, 4, 5, 6, 7])

def vertical(word):
    for p in word:
        print(p)

def verifica(peso):
    if peso <= 10:
        print('Preço de entrega é R$ 50,00')
    elif peso <= 20:
        print('Preço de entrega é R$ 80,00')
    else:
        print('Não é possível realizar a entrega desse produto.')