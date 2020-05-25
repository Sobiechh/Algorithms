inf = float("inf") #float inf

def floyd(weights):
    V = len(weights) #dlugosc wag
    distances = weights #przepisanie tablicy
    for k in range(V):
        temp_next = [list(row) for row in distances] #temp tab
        for i in range(V):
            for j in range(V):
                temp_next[i][j] = min( 
                    distances[i][j], distances[i][k] + distances[k][j] #sprawdzanie krotszej dorig
                )
        distances = temp_next 
    return distances


#przykadowy graf
graph = [[0, inf, inf, -3], [inf, 0, inf, 8], [inf, 4, 0, -2], [5, inf, 3, 0]]
print(floyd(graph))
graph = [[0, inf, -1, -3], [0, 0, inf, 10], [1, 4, 1, inf], [2,3,1,inf]]
print(floyd(graph))
