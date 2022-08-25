import heapq
import sys

input = sys.stdin.readline
print = sys.stdout.write

def main():
    heap = []
    n = int(input().rstrip())
    for _ in range(n):
        cmd = input().rstrip()
        if cmd == '0':
            if len(heap) == 0:
                print(str(0) + "\n")
            else:
                print(str(heapq.heappop(heap)) + "\n")
        else:
            heapq.heappush(heap,int(cmd))


if __name__ == "__main__":
    main()