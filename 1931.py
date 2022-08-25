import heapq
import sys

input = sys.stdin.readline
print = sys.stdout.write

def main():
    n = int(input().rstrip())
    n_list = list(range(n))
    for i in range(n):
        n_list[i] = list(map(int,input().rstrip().split()))
    n_list.sort(key=lambda x:(x[1],x[0]))
    
    ans = 0
    end = 0
    for item in n_list:
        if item[0] >= end:
            ans += 1
            end = item[1]
    
    print(str(ans) + "\n")

if __name__ == "__main__":
    main()