from itertools import permutations
from collections import deque

# 모든 경우의 수 찾기 -> ok
# 각 경우 실행
# BFS를 통한 최단 경로 찾기

# 각 경우의 수를 실행할 떄 마다 최솟값 갱신
# 만약 특정 경우를 실행시키는 데 현재 최솟값 보다 클 경우 해당 경우 종료

INF = 10000000
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def recursive(card_dict,subject_list,subject, cur_subject,i):
    # 정해진 순서 배열
    # 첫번째 or 두번째
    # 몇번째꺼 추가?
    if len(subject) * 2  == len(cur_subject):
        subject_list.append(cur_subject)
        return
    for j in range(2):
        if j == 0:
            recursive(card_dict,subject_list,subject,cur_subject + [card_dict[subject[i]][0],card_dict[subject[i]][1]],i+1)
        else:
            recursive(card_dict,subject_list,subject,cur_subject + [card_dict[subject[i]][1],card_dict[subject[i]][0]],i+1)

def shortest_path_bfs(board,cx,cy,tx,ty):
    queue = deque([])
    b_len = len(board)
    visited = [[False for _ in range(b_len)] for _ in range(b_len)]

    queue.append([cx,cy,0])
    while True:
        cx, cy, depth = queue.popleft()
        visited[cx][cy] = True
        if cx == tx and cy == ty:
            return depth
        for i in range(4):
            kx, ky = cx + dx[i], cy + dy[i]
            if 0 <= kx < b_len and 0 <= ky < b_len and not visited[kx][ky]:
                queue.append([kx,ky,depth + 1])
                should_append = False
                while board[kx][ky] == 0:
                    kx, ky = kx + dx[i], ky + dy[i]
                    if 0 > kx or kx >= b_len or 0 > ky or ky >= b_len:
                        kx, ky = kx - dx[i], ky - dy[i]
                        break
                    else:
                        should_append = True
                if should_append:
                    queue.append([kx,ky,depth + 1])

def research(board,path,r,c,min_cnt):
    ret = 0
    cx, cy = r, c
    for i in range(len(path)):
        if ret >= min_cnt:
            return INF
        tx, ty = path[i]
        ret += shortest_path_bfs(board,cx,cy,tx,ty) + 1
        cx, cy = tx, ty
        if i % 2 == 1:
            board[path[i][0]][path[i][1]] = 0
            board[path[i-1][0]][path[i-1][1]] = 0
    return ret

def solution(board, r, c):
    card_dict = {}
    card_value_list = []
    subject_list = []
    b_len = len(board)
    for i in range(b_len):
        for j in range(b_len):
            if board[i][j] != 0:
                if board[i][j] in card_dict:
                    card_dict[board[i][j]].append([i,j])
                else:
                    card_dict[board[i][j]] = [[i,j]]
                    card_value_list.append(board[i][j])
    
    for item in permutations(card_value_list,len(card_value_list)):
        recursive(card_dict,subject_list,list(item),[],0)

    min_cnt = INF
    for path in subject_list:
        temp_board = [item[:] for item in board]
        cnt = research(temp_board,path,r,c,min_cnt)
        min_cnt = min(min_cnt,cnt)

    return min_cnt

def main():
    graph = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
    r = 1
    c = 0
    print(solution(graph,r,c))


if __name__ == "__main__":
    main()