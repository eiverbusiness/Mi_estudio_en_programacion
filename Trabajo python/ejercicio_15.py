matriz_1 = [
    [1,3,5],
    [4,6,7],
    [8,9,2]
]

matriz_2 =[
    [9, 8, 7],
    [6, 5, 4],
    [3,2,1]
]

matriz_resultado = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(3):
    for j in range(3):
        matriz_resultado[i][j] = matriz_1[i][j] + matriz_2[i][j]
print("---Resultado de la Matriz---")
for fila in matriz_resultado:
    print(fila)