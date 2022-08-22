from collections import deque

def main():
    n = int(input())
    n_list = []
    for i in range(1,n+1):
        n_list.append(i)
    queue = deque(n_list)
    while len(queue) > 1:
        queue.popleft()
        item = queue.popleft()
        queue.append(item)
    print(queue.pop())


if __name__ == "__main__":
    main()