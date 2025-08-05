from matrizAdjacencias import MatrizAdjacencias
from listaAdjacencias import ListaAdjacencias
from dijkstra import dijkstra
from bellmanFord import bellman_ford
from floydWarshall import floyd_warshall
import info

if __name__ == "__main__":
    grafo = ListaAdjacencias(4)
    grafo.addAresta(0, 2, 5)
    grafo.addAresta(0, 3, 3)
    grafo.addAresta(1, 2, 2)
    grafo.addAresta(3, 1, 1)

    print(f"Ordem: {grafo.ordem()}")
    print(f"Tamanho: {grafo.tamanho()}")

    grafo.printGrafo()
    for i in range(grafo.numVertices):
        print(f"Vizinhos de {i}: {grafo.vizinhos(i)}")
    
    for i in range(grafo.numVertices):
        print(f"Grau do vertice {i}: {grafo.grau(i)}")

    print(f"Densidade: {info.densidade(grafo)}")

    print("Grafo complementar:")
    comp = info.complemento(grafo)
    comp.printGrafo()

    dist, prev = dijkstra(grafo, 0)
    print("Distâncias:", dist)
    print("Predecessores:", prev)

    dist, prev = bellman_ford(grafo, 0)
    print("Bellman-Ford Distâncias:", dist)
    print("Bellman-Ford Predecessores:", prev)

    dist, prev = floyd_warshall(grafo)

    print("Matriz de distâncias (Floyd-Warshall):")
    for linha in dist:
        print(linha)

    print("Matriz de predecessores (Floyd-Warshall):")
    for linha in prev:
        print(linha)