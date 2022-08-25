import heapq, sys

input = sys.stdin.readline
print = sys.stdout.write

def main():
    n = int(input().rstrip())
    heap = []
    for _ in range(n):
        cmd = int(input().rstrip())
        if cmd == 0:
            if len(heap) == 0:
                print("0\n")
            else:
                print(str(-heapq.heappop(heap)) + "\n")
        else:
            heapq.heappush(heap,-cmd)


if __name__ == "__main__":
    main()