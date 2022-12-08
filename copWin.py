# vertices  := lista de inteiros [0, ..., n-1]
# arestas   := lista de tuplas sinalizando conexão estre os vértices
# cop       := inteiro sinalizando um vértice
# robber    := inteiro sinalizando um vértice

def PermutationWrapper(listV: list, listC: list, n: int, listE) -> bool:
    if n == 1:
        print(listC)
        for v in listC:
            if NeighbourIntersection(v, listV, listE, len(listV)):
                print("Resultado okay")
                return True
    for v in listV:
        lista = listC + [v]
        listaaux = listV.copy()
        listaaux.remove(v)
        if PermutationWrapper(listaaux, lista, len(listV), listE):
            return True


def NeighbourIntersection(v1: int, listV: list, listE: tuple, n: int) -> bool:
    pointer: int = 0
    for i in listV:
        if i != v1:
            pointer += 1
        else:
            break
    for v in listV:
        if pointer > 0:
            pointer -= 1
            continue
        # criando as listas de vizinhos para os vértices vi e vj
        neighbors_i = listE[v1]
        neighbors_j = listE[v]
        # Logica para remoção de elemento reflexivo
        reAddElement: bool = False
        if v in neighbors_i:
            neighbors_i.remove(v)
            reAddElement = True
        # checagem de condição do teorema
        print("neighbors[i = ", v1, "]: ", neighbors_i)
        print("neighbors[j = ", v, "]: ", neighbors_j, "\n")

        conj = []
        for x in neighbors_i:
            if x in neighbors_j:
                conj.append(x)

        if not (all(x in conj for x in neighbors_i)):
            return False

        if reAddElement:
            neighbors_i.append(v)
            reAddElement = False
    return True


def copWin(vertices, arestas):
    n = len(vertices)
    neighbors = {}

    # criando dicionário contendo o conjunto de vértices vizinhos para
    # todo vértice vi do grafo
    for i in range(n):
        neighbors_i = []
        for j in range(len(arestas)):
            if arestas[j].count(i):
                if arestas[j].index(i) == 0:
                    neighbors_i.append(arestas[j][1])
                else:
                    neighbors_i.append(arestas[j][0])
        neighbors_i.sort()
        neighbors.update({i: neighbors_i})
    print(neighbors)

    # implementação do teorema 2.1
    PermutationWrapper(vertices,[],len(vertices),arestas)

# PermutationWrapper([0, 1, 2, 3], [], 4, [(0, 1), (0, 2), (1, 2), (2, 3), (3, 0), (3, 1)])
# um quadrado, não copwin
print(copWin([0, 1, 2, 3], [(0, 1), (1, 2), (2, 3), (3, 0)]))
print("\n")
print(copWin([0, 1, 2], [(0, 1), (1, 2), (2, 0)]))               # um triangulo, copwin
# print("\n")
# dois triangulos, copwin
# copWin([2, 0, 1, 3], [(0, 1), (0, 2), (1, 2), (2, 3), (3, 0), (3, 1)])
