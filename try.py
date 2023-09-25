colection_a = [1, 2, 3]
colection_b = [10, 20, 30]
                

result = [ (x + y) for x in range(len(colection_a)) for y in range(len(colection_b))]

print(result)

lista = (colection_a, colection_b)

print(lista)

suma = 0
for l in lista:
    for i in l:
        suma +=  i
print(suma)