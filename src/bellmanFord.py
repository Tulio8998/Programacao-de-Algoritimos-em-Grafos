from listaAdjacencias import ListaAdjacencias
from matrizAdjacencias import MatrizAdjacencias

def bellman_ford(grafo, s):
    n = grafo.ordem() # n vai está sendo o numero de vertices
    dist = [float('inf')] * n # vai esta iniciando a lista de distancia com infinito
    prev = [None] * n # A lista de predecessores com None
    dist[s] = 0
    prev[s] = s

    for k in range(n - 1):
        atualizou = False
        # Percorre todos os vertices u do grafo
        for u in range(n):
            # Atualiza a distancia de v e seu predecessor, se um caminho mais curto para v foi encontrado
            for v, peso in grafo.vizinhos(u):
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    prev[v] = u
                    atualizou = True
        if not atualizou:
            break

    return dist, prev # retorna as listas de distancias e predecessores
