from listaAdjacencias import ListaAdjacencias
from matrizAdjacencias import MatrizAdjacencias

def dijkstra(grafo, s):
    n = grafo.ordem()
    dist = [float('inf')] * n
    prev = [None] * n
    dist[s] = 0
    prev[s] = s

    O = list(range(n))
    C = []

    while O:
        u = min(O, key=lambda v: dist[v])
        O.remove(u)
        C.append(u)

        for v, peso in grafo.vizinhos(u):
            if v in O and dist[v] > dist[u] + peso:
                dist[v] = dist[u] + peso
                prev[v] = u

    return dist, prev