#Código Fonte
linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
print()

#Construção da Matriz
matriz = [0] * linhas

for i in range(linhas):
    matriz[i] = [0] * colunas

#Recebendo Valores
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = int(input(f'Digite o valor do a({i}, {j}): '))
    print()

#Mostrando Valores
for i in range(linhas):
    for j in range(colunas):
        print("  ", matriz[i][j], end="   ")
    print()
    print()