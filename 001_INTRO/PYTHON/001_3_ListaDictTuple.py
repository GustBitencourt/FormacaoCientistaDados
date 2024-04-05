lista = [1, 2, 3, "6", True]

list2 = [1, [2, 3, "6"], True]

list3 = list(range(0,5))
#comprimento da lista
print(list3)
print(len(list3))
list3[0] = 111
print(list3)

for n in range(0, len(list3)):
    print(list3[n])

#Dicionarios
notas = {
    'JP': 6.0,
    'Isa': 9.8,
    'PH': 3.4
}

print(notas['JP'])
#Todas as chaves e valores
notas.keys()
notas.values()

#verifica existencia
print('PH' in notas)
print('PV' in notas)

#apagar
del notas['PH']
print(notas)

#adicionar
notas['Ana'] = 7.7

#Busca valor, se não encontrar mostra o segundo parametro
notas.get('Alok', 'Não encontrado')

#Sets - não trás elementos repetidos
bigdata = {
    'Spark', 'Hive', 'Hadoop'
}

print('Spark' in notas)
#adiciona elemento
bigdata.add('Sqoop')

print(len(bigdata))


# Tuplas - listas não alteradas
tupla = (1, 2, 3, 4, 5, 6, 7)
print(tupla[3])
