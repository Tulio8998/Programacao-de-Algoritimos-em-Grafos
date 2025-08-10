from listaAdjacencias import ListaAdjacencias
from matrizAdjacencias import MatrizAdjacencias

def floyd_warshall(grafo):
    n = grafo.ordem() # n vai está sendo o numero de vertices
    dist = [[float('inf')] * n for _ in range(n)] # inicializa a matriz de distancia com infinito
    prev = [[None] * n for _ in range(n)] # E a matriz de predecessores com None

    for i in range(n):
        for j in range(n):
            if i == j:
                # A distancia de um vertice para ele mesmo e 0
                dist[i][j] = 0
                prev[i][j] = i
            elif grafo.possuiAresta(i, j):
                # Se existe uma aresta direta, a distancia e o peso dessa aresta
                peso = 0
                for vizinho, w in grafo.vizinhos(i):
                    if vizinho == j:
                        peso = w
                        break
                dist[i][j] = peso
                prev[i][j] = i
            else:
                 # caso nao haja aresta direta
                dist[i][j] = float('inf')
                prev[i][j] = None


    # Tenta encontrar um caminho melhor de i para j usando k como intermediario
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]

    return dist, prev # retorna as listas de distancias e predecessores