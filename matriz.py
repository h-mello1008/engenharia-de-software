#Código Fonte Principal
linhas = int(input("Digite a quantidade de linhas na matriz: "))
colunas = int(input("Digite a quantidade de colunas na matriz: "))
print()

#Construção da Matriz
matriz = [0] * linhas

for i in range(linhas):
    matriz[i] = [0] * colunas

#Recebe Valores
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = int(input(f'Digite o valor do a({i}, {j}): '))
    print()

#Mostra Valores
for i in range(linhas):
    for j in range(colunas):
        print("  ", matriz[i][j], end="   ")
    print()
    print()

#Posso substituir o range(linhas por range(matriz)) e range(colunas) por range(matriz[0]))