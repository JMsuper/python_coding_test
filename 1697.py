DP_list = []

def DP(n,k,cnt):
    stack = []
    stack.append([k,cnt])
    multiple_cond = n / 2
    while stack:
        cur_k, cur_cnt = stack.pop(-1)
        val = DP_list[n]
        if cur_k < 0 or cur_k > 200001 or DP_list[cur_k] <= cur_cnt or DP_list[n] <= cur_cnt:
            continue
        DP_list[cur_k] = cur_cnt
        if cur_k == n:
            continue
        if cur_k % 2 == 0 and abs(cur_k - n) > abs(cur_k//2 - n):
            stack.append([cur_k // 2,cur_cnt + 1])
            continue
        elif cur_k / 2 < multiple_cond:
            DP_list[n] = min(DP_list[n],cur_cnt + (n - cur_k))
            continue
        elif (n + multiple_cond) > cur_k > n:
            DP_list[n] = min(DP_list[n],cur_cnt + (cur_k - n))
            continue
        stack.append([cur_k + 1, cur_cnt + 1])
        stack.append([cur_k - 1, cur_cnt + 1])
        

def main():
    global DP_list
    n, k = map(int,input().split())
    DP_list = [200000 for _ in range(200001)]
    if n == k:
        print(0)
    elif n > k:
        print(n-k)
    else:
        DP(n,k,0)
        print(DP_list[n])

if __name__ == "__main__":
    main()