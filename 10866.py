from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write


def main():
    n = int(input())
    n_list = []
    for _ in range(n):
        n_list.append(input().rstrip().split())

    queue = deque([])
    
    for cmd_list in n_list:
        cmd = cmd_list[0]

        if cmd =="push_front":
            queue.appendleft(cmd_list[1])
        elif cmd == "push_back":
            queue.append(cmd_list[1])
        elif cmd == "pop_front":
            if len(queue) == 0:
                print("-1\n")
            else:
                print(queue.popleft() + "\n")
        elif cmd == "pop_back":
            if len(queue) == 0:
                print("-1\n")
            else:
                print(queue.pop() + "\n")
        elif cmd == "size":
            print(str(len(queue)) + "\n")
        elif cmd == "empty":
            if len(queue) == 0:
                print("1" + "\n")
            else:
                print("0" + "\n")
        elif cmd == "front":
            if len(queue) == 0:
                print("-1\n")
            else:
                print(queue[0] + "\n")
        elif cmd == "back":
            if len(queue) == 0:
                print("-1\n")
            else:
                print(queue[-1] + "\n")


if __name__ == "__main__":
    main()