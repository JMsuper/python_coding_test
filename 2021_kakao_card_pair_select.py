INF = int(1e9)

def floyd_warshall(graph):
    graph_len = len(graph)
    distance = graph[:]
    for i in range(graph_len):
        for j in range(graph_len):
            for k in range(graph_len):
                distance[j][k] = min(distance[j][k],distance[j][i] + distance[i][k])
    return distance


def create_graph(board):
    b_len = len(board)
    g_len = b_len * b_len
    graph = [[INF for _ in range(g_len)] for _ in range(g_len)]
    for i in range(g_len):
        graph[i][i] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(b_len):
        for j in range(b_len):
            for k in range(4):
                cx, cy = i + dx[k], j + dy[k]
                if 0 <= cx < b_len and 0 <= cy < b_len:
                    graph[b_len * i + j][b_len * cx + cy] = 1
                    while board[cx][cy] == 0:
                        cx, cy = cx + dx[k], cy + dy[k]
                        if 0 > cx or cx >= b_len or 0 > cy or cy >= b_len:
                            cx, cy = cx - dx[k], cy - dy[k]
                            break
                    graph[b_len * i + j][b_len * cx + cy] = 1
    return graph

            
def solution(board, r, c):
    answer = 0

    graph = create_graph(board)
    distance = floyd_warshall(graph)
    print(distance)

    return answer



def main():
    graph = [
        [1,1,0],
        [0,3,3],
        [2,0,2]
    ]
    r = 1
    c = 1
    solution(graph,r,c)
    # board = [
    #     [1,1,0],
    #     [0,3,3],
    #     [2,0,2]
    # ]

    # graph_t = create_graph(board)

    # graph = [
    #     [ 0 , 1 ,INF, 1 ,INF,INF, 1 ,INF,INF],
    #     [ 1 , 0 , 1 ,INF, 1 ,INF,INF,INF,INF],
    #     [INF, 1 , 0 ,INF,INF, 1 ,INF,INF,INF],
    #     [ 1 ,INF,INF, 0 , 1 ,INF, 1 ,INF,INF],
    #     [INF, 1 ,INF, 1 , 0 , 1 ,INF, 1 ,INF],
    #     [INF, 1 ,INF,INF, 1 , 0 ,INF,INF, 1 ],
    #     [ 1 ,INF,INF, 1 ,INF,INF, 0 , 1 , 1 ],
    #     [INF,INF,INF,INF, 1 ,INF, 1 , 0 , 1 ],
    #     [INF,INF,INF,INF,INF, 1 , 1 , 1 , 0 ],
    # ]

if __name__ == "__main__":
    main()