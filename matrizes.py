matriz = [
    [3, 8, 1],
    [4, 9, 6],
    [2, 7, 5]
]

print("=== EXIBIÇÃO DA MATRIZ EM FORMATO DE GRADE ===")
for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]}]", end=" ")
    print()

print(f"Elemento na Linha 0 e Coluna 1: {matriz[0][1]}")
print(f"Elemento na Linha 2 e Coluna 2: {matriz[2][2]}")

soma_diagonal = 0
for l in range(3):
    for c in range(3):
        if l == c:
            soma_diagonal += matriz[l][c]

print(f"Soma dos elementos da Diagonal Principal: {soma_diagonal}")
