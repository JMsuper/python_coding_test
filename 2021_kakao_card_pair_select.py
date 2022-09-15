from copy import deepcopy


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

def recursive(card_dict,board,cnt,cx,cy):
    b_len = len(board)
    graph = create_graph(board)
    distance = floyd_warshall(graph)
    target_subject_dict = {}
    for key, value in card_dict.items():
        for x, y in value:
            target_subject_dict[(x,y)] = distance[cx * b_len + cy][x * b_len + y]
    for key, value in target_subject_dict.items():
        for item in card_dict[board[key[0]][key[1]]]:
            if item[0] != key[0] or item[1] != key[1]:
                target_subject_dict[key] = value + distance[key[0] * b_len + key[1]][item[0] * b_len + item[1]] 
    subject_list = []
    t_distance = INF
    for key, value in target_subject_dict.items():
        if value < t_distance:
            subject_list = [[key[0],key[1]]]
            t_distance = value
            continue
        elif value == t_distance:
            subject_list.append([key[0],key[1]])
    
    min_ret = INF
    for item in subject_list:
        cx, cy = item[0], item[1]
        card_value = board[cx][cy]
        copy_board = deepcopy(board)
        copy_card_dict = deepcopy(card_dict)
        for x,y in card_dict[card_value]:
            copy_board[x][y] = 0
        del copy_card_dict[card_value]
        if copy_card_dict:
            ret = recursive(copy_card_dict,copy_board,cnt + t_distance + 2, cx, cy)
            if ret < min_ret:
                min_ret = ret
    if min_ret == INF:
        return cnt + t_distance + 2
    else:
        return min_ret


            
def solution(board, r, c):
    answer = 0
    card_dict = {}
    b_len = len(board)
    for i in range(b_len):
        for j in range(b_len):
            if board[i][j] != 0:
                if board[i][j] in card_dict:
                    card_dict[board[i][j]].append([i,j])
                else:
                    card_dict[board[i][j]] = [[i,j]]
    cx, cy = r, c
    answer = recursive(card_dict,board,0,cx,cy)
    return answer



def main():
    graph = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]	
    r = 0
    c = 1
    print(solution(graph,r,c))


if __name__ == "__main__":
    main()