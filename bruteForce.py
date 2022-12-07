# vertices  := lista de inteiros [0, ..., n-1]
# arestas   := lista de tuplas sinalizando conexão estre os vértices
# cop       := inteiro sinalizando um vértice
# robber    := inteiro sinalizando um vértice

from queue import Queue

# se for copwin, o algoritmo computa todos os movimentos. caso contrário,
# roda indefinidamente
def bruteForce(vertices, arestas, cop, robber):
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
        neighbors.update({i:neighbors_i})
    print(neighbors)

    while cop != robber:
        neighbors_cop = neighbors[cop]
        print(neighbors_cop)
        distance_to_robber = distances(neighbors, robber)
        print(distance_to_robber)
        move_cop = 999999999
        
        #cop move
        for i in neighbors_cop:
            if distance_to_robber[i] <= move_cop:
                move_cop = distance_to_robber[i]
                cop = i

        if cop == robber:
            return 1

        neighbors_robber = neighbors[robber]
        print(neighbors_robber)
        distance_to_cop = distances(neighbors, cop)
        print(distance_to_cop)
        move_robber = 0

        #robber move
        for i in neighbors_robber:
            if distance_to_cop[i] >= move_robber:
                move_robber = distance_to_cop[i]
                robber = i
    return 1

def distances(neighbors, source):
    Q = Queue()
    distance_dict = {k: 999999999 for k in neighbors.keys()}
    visited_vertices = list()
    Q.put(source)
    visited_vertices.append(source)
    while not Q.empty():
        vertex = Q.get()
        if vertex == source:
            distance_dict[vertex] = 0
        for u in neighbors[vertex]:
            if u not in visited_vertices:
                # update the distance
                if distance_dict[u] > distance_dict[vertex] + 1:
                    distance_dict[u] = distance_dict[vertex] + 1
                Q.put(u)
                visited_vertices.append(u)
    return distance_dict

# print(bruteForce([0,1,2,3], [(0,1),(1,2),(2,3),(3,0)], 1, 3))       # um quadrado, não copwin
# print(bruteForce([0,1,2], [(0,1),(1,2),(2,0)], 1, 2))               # um triangulo, copwin
# print(bruteForce([0,1,2,3], [(0,1),(1,2),(2,3),(3,0),(3,1)], 1, 3)) #dois triangulos, copwin