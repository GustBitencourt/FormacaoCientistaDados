def impressao():
    print('Print de função')

impressao()

#com parametro
def imprimi(n):
    print(n)

imprimi('BBMP')

def potencia(n):
    return n * n

def intervalo(i=1, f=10):
    for n in range(i, f+2):
        print(n)

x = intervalo(1,10)
y = intervalo()