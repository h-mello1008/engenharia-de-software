#Código Fonte Principal
l = int(input("Digite o número de linhas: "))
c = int(input("Digite o número de colunas: "))
e = int(input("Digite o valor do escalar: "))
print()

#Contrução da Matriz
m = [0] * l

for i in range(l):
    m[i] = [0] * c

#Recebe Valores
for i in range(l):
    for j in range(c):
        m[i][j] = int(input(f'Digite o valor do a({i}, {j}): '))
    print()

#Mostra Valores
print(f'Matriz Original')
print()
for i in range(l):
    for j in range(c):
        print("  ", m[i][j], end="   ")
    print()
    print()

#Multiplicando pelo Escalar
for i in range(l):
    for j in range(c):
        m[i][j] *= e

#Mostra Valores
print(f'Matriz Final')
print()
for i in range(l):
    for j in range(c):
        print("  ", m[i][j], end="   ")
    print()
    print()