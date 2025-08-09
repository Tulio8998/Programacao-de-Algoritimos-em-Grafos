from listaAdjacencias import ListaAdjacencias
from matrizAdjacencias import MatrizAdjacencias

def floyd_warshall(grafo):
    n = grafo.ordem()
    dist = [[float('inf')] * n for _ in range(n)]
    prev = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
                prev[i][j] = i
            elif grafo.possuiAresta(i, j):
                peso = 0
                for vizinho, w in grafo.vizinhos(i):
                    if vizinho == j:
                        peso = w
                        break
                dist[i][j] = peso
                prev[i][j] = i
            else:
                dist[i][j] = float('inf')
                prev[i][j] = None

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]

    return dist, prev