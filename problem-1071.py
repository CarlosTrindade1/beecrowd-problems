x = int(input())
y = int(input())

soma = 0

# Ordenar os números em ordem crescente
if (x > y):
    aux = y
    y = x
    x = aux

for i in range(x + 1, y):
    if (i % 2 != 0):
        soma += i

print(soma)