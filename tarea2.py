import random
w = 100  #peso maximo
n = 100000  #Cantidad de objetos
objetos = []  #[valor,peso]
matriz = []
for i in range(0,n):  #Da valores aleatorios a los objetos
    objetos.append([random.randrange(20),random.randrange(15)])
for i in range(n + 1):  #Crea la matriz
    matriz.append([])
    for j in range(w + 1):
        matriz[i].append(None)
for i in range(0, n + 1):  #Rellena la columna 0 con 0
    matriz[i][0] = 0
for i in range(0, w + 1):  #Rellena la fila 0 con 0
    matriz[0][i] = 0
for i in range(1,n+1):  #Algoritmo que recorre y rellena la matriz
    for j in range(1,w+1):
        if objetos[i-1][1] <= j:
            if objetos[i-1][0] + matriz[i-1][j-objetos[i-1][1]] > matriz[i-1][j]:
                matriz[i][j] = objetos[i-1][0] + matriz[i-1][j-objetos[i-1][1]]
            else:
                matriz[i][j] = matriz[i - 1][j]
        else:
            matriz[i][j] = matriz[i - 1][j]
maximo_valor = matriz[n][w]  #El ultimo elemento de la matriz es el valor maximo alcanzable
pkt = []  #Lista donde se agregaran los elementos que componen la solucion
while n > 0:  #Este algoritmo recorre la matriz para encontrar los objetos que arman la solucion
    if matriz[n][w] != matriz[n-1][w]:
        pkt.append(n)
        w = w-objetos[n-1][1]
        n = n-1
    else:
        n = n-1
