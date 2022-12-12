# Implementação do Jogo Polícia e Ladrão em Grafos
# Discentes: Kaio Rodrigo, João Lucas Melo e Thiago Andrade
# Docente: Roberto Parente
# Disciplina: Teoria dos Grafos
# Instituição: Universidade Federal da Bahia
# Departamento: Ciência da Computação

def PermutationWrapper(listV: list, listC: list, n: int, listE: dict) -> bool:
    if n == 1:
        #print(listC)
        if TheoremCondition(listE, listC):
            return True
    for v in listV:
        lista = listC + [v]
        listaaux = listV.copy()
        listaaux.remove(v)
        if PermutationWrapper(listaaux, lista, len(listV), listE):
            return True


# Operação: Ni(V) = N(v) ^ vj: i <= j <= n
def NeighbourIntersection(v1: int, v2:int , listV: list, listE: dict) -> list:
    neighbors_i = listE[v2]
    conj = []
    for v in listV:
        if v1 > 0:
            v1 -= 1
            continue
        if v in neighbors_i:
            conj.append(v)
   # print(conj)
    return conj


def SubsetComparison(list1: list, list2: list) -> bool:  # LIST1 IS SUBSET OF LIST2
    for x in list1:
        if not x in list2:
            return False
    return True


def TheoremCondition(listE: dict, listV: list):
    for v1 in range(0, len(listV)):
        for v2 in range(v1 + 1, len(listV)):
            subsetv1 = NeighbourIntersection(
                v1, listV[v1], listV, listE)
            subsetv2 = NeighbourIntersection(
                v1, listV[v2], listV, listE)
            #print("v1:", listV[v1], "subset", subsetv1)
            #print("v2:", listV[v2], "subset", subsetv2)
            if (not SubsetComparison(subsetv1, subsetv2)):
                #print("Subset falso")
                return False
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
    #print(neighbors)
    # implementação do teorema 2.1
    if PermutationWrapper(vertices, [], len(vertices), neighbors):
        return 1 #Cop Win
    else:
        return 0 #Robbers Win

# PermutationWrapper([0, 1, 2, 3], [], 4, [(0, 1), (0, 2), (1, 2), (2, 3), (3, 0), (3, 1)])


# um quadrado, não copwin
# print("\n")
print(copWin([0, 1, 2], [(0, 1), (1, 2), (2, 0), (0,0), (1,1), (2,2)]))               # um triangulo, copwin
# print("\n")
# dois triangulos, copwin
print(copWin([0, 1, 2, 3], [(0, 1), (1, 2), (2, 3), (3, 0), (0,0), (1,1), (2,2), (3,3)])) # um quadrado, robbers win
# PARA CADA V EM LISTVERTORD SE VIZINHOSINTERSECAO RETONRAR VERDADEIRA, A CONDIÇÃO DO TEOREMA E VERDADE
