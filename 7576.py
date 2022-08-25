from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

board = []
tomato_queue = []
tomato_cnt = 0

def is_complted(m,n):
    global board
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                return False
    return True

def find_completed_tomato(m,n):
    global board, tomato_queue, tomato_cnt
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                tomato_queue.append([i,j,0])
                tomato_cnt += 1
            elif board[i][j] == 0:
                tomato_cnt += 1
    

def BFS(m,n):
    global board, tomato_queue, tomato_cnt
    find_completed_tomato(m,n)
    queue = deque(tomato_queue)

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    completed_tomato_cnt = len(queue)
    ans = 0
    while queue:
        cx, cy, day = queue.popleft()
        ans = max(ans,day)
        if completed_tomato_cnt == tomato_cnt:
            break
        for i in range(4):
            tx, ty = cx + dx[i], cy + dy[i]
            if 0 <= tx < n and 0 <= ty < m:
                if board[tx][ty] == 0:
                    queue.append([tx,ty,day + 1])
                    completed_tomato_cnt += 1
                    board[tx][ty] = 1
    if queue:
        ans = max(ans,queue.pop()[2])
    return ans

def main():
    global board
    m, n = map(int,input().rstrip().split())
    board = list(range(n))
    for i in range(n):
        board[i] = list(map(int,input().rstrip().split()))
    if is_complted(m,n):
        print("0\n")
    else:
        ans = BFS(m,n)
        if is_complted(m,n):
            print(str(ans) + "\n")
        else:
            print("-1\n")

if __name__ == "__main__":
    main()