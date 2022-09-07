import copy

# 이기면 True, 지면 False
def DFS_a(board, aloc, bloc, cnt):
    global len_x, len_y, dx, dy
    if board[aloc[0]][aloc[1]] == 0:
        return [False, cnt]
    is_over = True
    ret_list = []
    for i in range(4):
        tx, ty = aloc[0] + dx[i], aloc[1] + dy[i]
        if 0 <= tx < len_x and 0 <= ty < len_y and board[tx][ty] == 1:
            temp_board = copy.deepcopy(board)
            temp_board[aloc[0]][aloc[1]] = 0
            ret_list.append(DFS_b(temp_board,[tx,ty],bloc,cnt+1))
            is_over = False
    if is_over:
        return [False, cnt]
    win_cnt, min_cnt, max_cnt = 0, 99999999, 0
    for a_lose, cnt in ret_list:
        if not a_lose:
            win_cnt += 1
            min_cnt = min(min_cnt,cnt)
        max_cnt = max(max_cnt,cnt)
    if win_cnt == 0:
        return False, max_cnt
    else:
        return True, min_cnt



def DFS_b(board, aloc, bloc, cnt):
    global len_x, len_y, dx, dy
    if board[bloc[0]][bloc[1]] == 0:
        return [False, cnt]
    is_over = True
    ret_list = []
    for i in range(4):
        tx, ty = bloc[0] + dx[i], bloc[1] + dy[i]
        if 0 <= tx < len_x and 0 <= ty < len_y and board[tx][ty] == 1:
            temp_board = copy.deepcopy(board)
            temp_board[bloc[0]][bloc[1]] = 0
            ret_list.append(DFS_a(temp_board,aloc,[tx,ty],cnt+1))
            is_over = False
    if is_over:
        return [False, cnt]
    win_cnt, min_cnt, max_cnt = 0, 1000, 0
    for b_lose, cnt in ret_list:
        if not b_lose:
            win_cnt += 1
            min_cnt = min(min_cnt,cnt)
        max_cnt = max(max_cnt,cnt)
    if win_cnt == 0:
        return False, max_cnt
    else:
        return True, min_cnt


def solution(board, aloc, bloc):
    global len_x, len_y, dx, dy
    answer = -1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    len_x = len(board)
    len_y = len(board[0])
    win, answer =  DFS_a(board,aloc,bloc,0)
    return answer

def main():
    board =[[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]
    aloc = [0, 0]
    bloc = [3, 3]
    print(solution(board,aloc,bloc))

if __name__ == "__main__":
    main()