import copy

def floyd_warshall(graph):
    INF = int(1e9)
    graph_len = len(graph)
    
    distance = [[0 for _ in range(graph_len)] for _ in range(graph_len)]
    for i in range(graph_len):
        for j in range(graph_len):
            distance[i][j] = graph[i][j]
    
    for i in range(graph_len):
        for j in range(graph_len):
            for k in range(graph_len):
                distance[j][k] = min(distance[j][k],distance[j][i] + distance[i][k])
    return distance

def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e9)
    graph = [[INF for _ in range(n)] for _ in range(n)]
    for x,y,dist in fares:
        graph[x-1][y-1] = dist
        graph[y-1][x-1] = dist
    distance = floyd_warshall(graph)
    
    min_dist = distance[s-1][a-1] + distance[s-1][b-1]
    for i in range(n):
        new_distance = 0
        if i != a-1 and i != b-1:
            new_distance = distance[s-1][i]+distance[i][a-1]+distance[i][b-1]
        elif i == a-1:
            new_distance = distance[s-1][i] + distance[i][b-1]
        elif i == b-1:
            new_distance = distance[s-1][i] + distance[i][a-1]
        min_dist = min(min_dist,new_distance)
    answer = min_dist
    
    return answer

def main():
    n = 6
    s = 4
    a = 6
    b = 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n,s,a,b,fares))

if __name__ == "__main__":
    main()