def prod_diag(matriz):
    prod = 1
    for i in range(len(matriz)):
        prod *= matriz[i][i]
    return prod

def diag_princ(matriz):
    diagonal = []
    for i in range(min(len(matriz), len(matriz[0]))):  
        diagonal.append(matriz[i][i])
    return diagonal


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
print("Matriz Original")
print()
for i in range(linhas):
    for j in range(colunas):
        print("  ", matriz[i][j], end="   ")
    print()
    print()

#Produto da Diagonal
if linhas == colunas:
    print(f'O produto da diagonal principal é: {prod_diag(matriz)}')
    print(diag_princ(matriz))

elif linhas != colunas:
    print("O número de linhas e colunas é diferente, portanto não é possível fazer o produto da diagonal principal")

else:
    print("Erro")