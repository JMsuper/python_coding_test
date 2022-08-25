from itertools import permutations

DP_list = [0 for _ in range(11)]
DP_list[1] = 1
DP_list[2] = 2
DP_list[3] = 4

def DP(n):
    global DP_list
    if DP_list[n] > 0:
        return DP_list[n]
    DP_list[n] = DP(n-1) + DP(n-2) + DP(n-3)
    return DP_list[n] 


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(DP(n))


if __name__ == "__main__":
    main()