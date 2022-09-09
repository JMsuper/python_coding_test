INF = int(1e9)

def floyd_warshall(graph):
    graph_len = len(graph)
    distance = graph[:]
    
    for i in range(graph_len):
        for j in range(graph_len):
            for k in range(graph_len):
                distance[j][k] = min(distance[j][k],distance[j][i] + distance[i][k])
    return distance


def main():
    graph = [
        [0,5,INF,8],
        [7,0,9,INF],
        [2,INF,0,4],
        [INF,INF,3,0]
    ]
    distance = floyd_warshall(graph)
    print(distance)

if __name__ == "__main__":
    main()