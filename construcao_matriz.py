#Código Fonte Principal
nrLinhas = int(input("Digite o número de linha: "))
nrColunas = int(input("Digite o número de colunas: "))
print()

#Construção da Matriz
matriz = [0] * nrLinhas

for i in range(nrLinhas):
    matriz[i] = [0] * nrColunas

#Recebe Valores
for i in range(nrLinhas):
    for j in range(nrColunas):
        matriz[i][j] = int(input(f'Digite o valor do a({i}, {j}): '))
    print()

#Mostra Valores
for i in range(nrLinhas):
    for j in range(nrColunas):
        print("  ", matriz[i][j], end="   ")
    print()
    print()