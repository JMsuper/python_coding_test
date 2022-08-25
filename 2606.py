from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

def main():
    n = int(input().rstrip())
    m = int(input().rstrip())
    linked_list = [[] for _ in range(n+1)]
    for _ in range(m):
        start, end = map(int,input().rstrip().split())
        linked_list[start].append(end)
        linked_list[end].append(start)
    visited = set([])
    queue = deque([1])
    while queue:
        node = queue.popleft()
        visited.add(node)
        for item in linked_list[node]:
            if not item in visited:
                visited.add(item)
                queue.append(item)
    print(str(len(visited)-1) + "\n")

if __name__ == "__main__":
    main()