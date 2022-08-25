import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

visited = []
linked_list = []

def BFS(start):
    global visited, linked_list
    queue = deque([])
    queue.appendleft(start)
    while queue:
        node = queue.popleft()
        if visited[node] == 0:
            visited[node] = 1
            for item in linked_list[node]:
                queue.appendleft(item)

def main():
    global visited, linked_list
    n, m = map(int,input().rstrip().split())
    visited = [0 for i in range(n+1)]
    linked_list = [[] for i in range(n+1)]
    ans = 0
    for _ in range(m):
        start, end = map(int,input().rstrip().split())
        linked_list[start].append(end)
        linked_list[end].append(start)
    
    for i in range(1,n+1):
        if visited[i] == 1:
            continue
        else:
            BFS(i)
            ans += 1
    print(str(ans) + "\n")




        
if __name__ == "__main__":
    main()