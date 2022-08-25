import sys

input = sys.stdin.readline
print = sys.stdout.write

DP_list = []

def DP(n):
    global DP_list
    if DP_list[n] > 0:
        return DP_list[n]
    result = DP(n-1) + DP(n-2)
    DP_list[n] = result
    return result

def main():
    global DP_list
    n = int(input().rstrip())
    DP_list = [0 for _ in range(n+1)]
    DP_list[1] = 1
    if n > 1:
        DP_list[2] = 2
    print(str(DP(n) % 10007) + "\n")

if __name__ == "__main__":
    main()