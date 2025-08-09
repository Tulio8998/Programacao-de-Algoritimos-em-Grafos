import listaAdjacencias
import matrizAdjacencias

# retorna a densidade do grafo:
def densidade(grafo):
    maxArestas = grafo.numVertices * (grafo.numVertices - 1)
    return float(grafo.numArestas) / float(maxArestas)

# retorna o complemento do grafo:
def complemento(grafo):
    comp = listaAdjacencias.ListaAdjacencias(grafo.numVertices)

    for v1 in range(grafo.numVertices):
        for v2 in range(grafo.numVertices):
            if (not grafo.possuiAresta(v1, v2)) and v1 != v2:
                comp.addAresta(v1, v2)
    return comp

# retorna True se o grafo eh completo:
def completo(grafo):
    for i in range(grafo.ordem()):
        for j in range(grafo.ordem()):
            if not grafo.possuiAresta(i, j):
                return False
    return True

# retorna True se o grafo eh regular:
def regular(grafo):
    grau = grafo.grau(0)
    for i in range(grafo.ordem()):
        if grafo.grau(i) != grau:
            return False
    return True

# retorna um subgrafo induzido pelo conjunto de vertices:
def subgrafo(grafo, vertices):
    sg = listaAdjacencias.ListaAdjacencias(len(vertices))

    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i != j and grafo.possuiAresta(vertices[i], vertices[j]):
                sg.addAresta(i, j)
    return sg
