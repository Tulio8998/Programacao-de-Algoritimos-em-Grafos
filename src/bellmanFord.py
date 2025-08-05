from listaAdjacencias import ListaAdjacencias
from matrizAdjacencias import MatrizAdjacencias

def bellman_ford(grafo, s):
    n = grafo.ordem()
    dist = [float('inf')] * n
    prev = [None] * n
    dist[s] = 0
    prev[s] = s

    for k in range(n - 1):
        atualizou = False
        for u in range(n):
            for v, peso in grafo.vizinhos(u):
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    prev[v] = u
                    atualizou = True
        if not atualizou:
            break

    return dist, prev
