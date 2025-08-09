import sys
import time
import tracemalloc
from listaAdjacencias import ListaAdjacencias
from dijkstra import dijkstra
from bellmanFord import bellman_ford
from floydWarshall import floyd_warshall

def ler_grafo_dimacs(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        primeira_linha = f.readline().strip().split()
        num_vertices = int(primeira_linha[0])
        
        grafo = ListaAdjacencias(num_vertices)
        
        for linha_aresta in f:
            linha_aresta = linha_aresta.strip()
            if not linha_aresta:
                continue

            partes_a = linha_aresta.split()
            origem = int(partes_a[0])
            destino = int(partes_a[1])
            peso = int(partes_a[2]) if len(partes_a) > 2 else 1
            grafo.addAresta(origem, destino, peso) 
    return grafo

def reconstruir_caminho(prev, origem, destino):
    caminho = []
    predecessores = prev[origem] if isinstance(prev[0], list) else prev
    if predecessores[destino] is None:
        return None

    atual = destino
    for _ in range(len(predecessores)): 
        caminho.insert(0, atual)
        if atual == origem:
            break
        atual = predecessores[atual]
        if atual is None:
            return None 
    
    if caminho[0] != origem:
        return None
    return caminho

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python main.py <arquivo_grafo> <vertice_origem> <vertice_destino>")
        sys.exit(1)

    arquivo_grafo = sys.argv[1]
    vertice_origem = int(sys.argv[2])
    vertice_destino = int(sys.argv[3])
    print("Processando...")
    grafo = ler_grafo_dimacs(arquivo_grafo)
    
    print("Algoritmo de Dijkstra:")
    tracemalloc.start()
    tempo_inicio = time.time()
    dist_d, prev_d = dijkstra(grafo, vertice_origem)
    tempo_fim = time.time()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    caminho_d = reconstruir_caminho(prev_d, vertice_origem, vertice_destino)
    custo_d = dist_d[vertice_destino]

    if caminho_d:
        print(f"Caminho mínimo: {caminho_d}")
    else:
        print("Caminho mínimo: Nao ha caminho")
        
    print(f"Custo: {custo_d if custo_d != float('inf') else 'infinito'}")
    print(f"Tempo execução: {tempo_fim - tempo_inicio:.6f} s")
    print(f"Memória utilizada: {memoria_pico / 1024 / 1024:.6f} MB\n")

    print("Algoritmo de Bellman-Ford:")
    tracemalloc.start()
    tempo_inicio = time.time()
    dist_bf, prev_bf = bellman_ford(grafo, vertice_origem)
    tempo_fim = time.time()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    caminho_bf = reconstruir_caminho(prev_bf, vertice_origem, vertice_destino)
    custo_bf = dist_bf[vertice_destino]

    if caminho_bf:
        print(f"Caminho mínimo: {caminho_bf}")
    else:
        print("Caminho mínimo: Nao ha caminho")
        
    print(f"Custo: {custo_bf if custo_bf != float('inf') else 'infinito'}")
    print(f"Tempo execução: {tempo_fim - tempo_inicio:.6f} s")
    print(f"Memória utilizada: {memoria_pico / 1024 / 1024:.6f} MB\n")


    print("Algoritmo de Floyd-Warshall:")
    tracemalloc.start()
    tempo_inicio = time.time()
    dist_fw, prev_fw = floyd_warshall(grafo)
    tempo_fim = time.time()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    caminho_fw = reconstruir_caminho(prev_fw, vertice_origem, vertice_destino)
    custo_fw = dist_fw[vertice_origem][vertice_destino]

    if caminho_fw:
        print(f"Caminho mínimo: {caminho_fw}")
    else:
        print("Caminho mínimo: Nao ha caminho")
        
    print(f"Custo: {custo_fw if custo_fw != float('inf') else 'infinito'}")
    print(f"Tempo execução: {tempo_fim - tempo_inicio:.6f} s")
    print(f"Memória utilizada: {memoria_pico / 1024 / 1024:.6f} MB")