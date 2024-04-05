#Decisão
nota = 7
if nota >= 7:
    print("Passou")
else:
    print("Reprovado")

if nota <= 4:
    print("Reprovado")
elif nota < 7:
    print("Exame")
else:
    print("Aprovado")


#Repetição
count = 0
while count <= 5:
    print(count)
    count += 1

#range(0, 10, 1)
#range(inicio, parada, incremento)
for n in range(1, 11):
    print(n + 1)

for n in range(10, 0, -1):
    print(n)

for n in range(10, 0, -1):
    if n == 4:
        break
    print(n)

for n in range(10, 0, -1):
    if n == 4:
        continue
    print(n)