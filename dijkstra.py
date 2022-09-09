
# 인접행렬 이용
# param : 2차원 그래프
# return : 각 노드 최소 비용 리스트
INF = int(1e9)

def dijkstra_matrix(graph,start):
    node_len = len(graph)
    visited = [False for _ in range(node_len)]
    distance = [INF for _ in range(node_len)]
    distance[start] = 0
    
    while True:
        min_distance = INF
        min_node = -1
        for i in range(node_len):
            if distance[i] < min_distance and not visited[i]:
                min_distance = distance[i]
                min_node = i
        if min_node == -1:
            break
        visited[min_node] = True
        for i in range(node_len):
            distance[i] = min(distance[i],graph[min_node][i] + distance[min_node])
    return distance
            

# 인접리스트 이용
# param : 인접 리스트
# return : 각 노드 최소 비용 리스트
def dijkstra_adj_list(adj_list,start):
    node_len = len(adj_list)
    visited = [False for _ in range(node_len)]
    distance = [INF for _ in range(node_len)]
    distance[start] = 0
    
    while True:
        min_distance = INF
        min_node = -1
        for i in range(node_len):
            if distance[i] < min_distance and not visited[i]:
                min_distance = distance[i]
                min_node = i
        if min_node == -1:
            break
        visited[min_node] = True
        for v, dist in adj_list[min_node]:
            distance[v] = min(distance[v],dist + distance[min_node])
    return distance



def main():
    graph = [
        [0,2,5,1,INF,INF],
        [2,0,3,2,INF,INF],
        [5,3,0,3,1,5],
        [1,2,3,0,1,INF],
        [INF,INF,1,1,0,2],
        [INF,INF,5,INF,2,0]
    ]
    distance_matrix = dijkstra_matrix(graph,0)
    print(distance_matrix)

    adj_list = [
        [[1,2],[2,5],[3,1]],
        [[0,2],[2,3],[3,2]],
        [[0,5],[1,3],[3,3],[4,1],[5,5]],
        [[0,1],[1,2],[2,3],[4,1]],
        [[2,1],[3,1],[5,2]],
        [[2,5],[4,2]]
    ]
    distance_adj = dijkstra_adj_list(adj_list,0)
    print(distance_adj)

if __name__ == "__main__":
    main()