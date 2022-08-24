from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

def main():
    n = int(input().rstrip())
    queue = deque([])
    for _ in range(n):
        cmd_list = input().rstrip().split()
        cmd = cmd_list[0]
        
        if cmd == "push":
            queue.append(cmd_list[1])
            continue
        elif cmd == "pop":
            if len(queue) == 0:
                print("-1" + "\n")
            else:
                print(queue.popleft() + "\n")
            continue
        elif cmd == "size":
            print(str(len(queue)) + "\n")
            continue
        elif cmd == "empty":
            if len(queue) == 0:
                print("1" + "\n")
            else:
                print("0" + "\n")
            continue
        elif cmd == "front":
            if len(queue) == 0:
                print("-1" + "\n")
            else:
                print(queue[0] + "\n")
            continue
        elif cmd == "back":
            if len(queue) == 0:
                print("-1" + "\n")
            else:
                print(queue[-1] + "\n")
            continue

if __name__ == "__main__":
    main()