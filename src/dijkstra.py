from listaAdjacencias import ListaAdjacencias
from matrizAdjacencias import MatrizAdjacencias

def dijkstra(grafo, s):
    n = grafo.ordem() # n vai está sendo o numero de vertices
    dist = [float('inf')] * n # vai esta iniciando a lista de distancia com infinito
    prev = [None] * n # A lista de predecessores com None
    dist[s] = 0
    prev[s] = s

    O = list(range(n)) # vertices nao visitados
    C = [] # vertices ja visitados

    while O: # Enquanto houver vertices abertas
        u = min(O, key=lambda v: dist[v]) # Vertice com menor distancia em O 
        # É removido o vertice dos abertos e adiciona aos fechados
        O.remove(u)
        C.append(u)

        # Verifica se para cada vizinho v de u, se ainda esta aberto e um caminho mais curto foi encontrado
        for v, peso in grafo.vizinhos(u):
            if v in O and dist[v] > dist[u] + peso:
                dist[v] = dist[u] + peso
                prev[v] = u

    return dist, prev # retorna as listas de distancias e predecessores