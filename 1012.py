from collections import deque
import sys

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]
board = []
visited = []
baechu_list = []

def find_warm_cnt(m, n):
    global board, baechu_list, visited
    def bfs(x,y):
        queue = deque([])
        queue.append([y,x])
        cy, cx = y, x
        while queue:
            cy, cx = queue.popleft()
            visited[cy][cx] = 1
            for i in range(4):
                ty, tx = cy + dy[i], cx + dx[i]
                if 0 <= ty < n and 0 <= tx < m and not [ty,tx] in queue and board[ty][tx] == 1 and visited[ty][tx] == 0:
                    queue.append([ty,tx])

    visited = list(range(n))
    for i in range(n):
        visited[i] = [0 for _ in range(m)]
    ans = 0

    for y, x in baechu_list:
        if visited[y][x] == 0:
            bfs(x,y)
            ans += 1
    return ans

def main():
    global board, baechu_list, visited
    t = int(input().rstrip())
    for i in range(t):
        m,n,k = map(int,input().rstrip().split())
        board = list(range(n))
        baechu_list = list(range(k))
        for j in range(n):
            board[j] = [0 for _ in range(m)]


        for j in range(k):
            x, y = map(int,input().rstrip().split())
            baechu_list[j] = [y,x]
            board[y][x] = 1
        
        print(find_warm_cnt(m,n))
    
if __name__ == "__main__":
    main()