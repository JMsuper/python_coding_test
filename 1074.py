blk_dist_list = []

def DQ(cn,r,c):
    global blk_dist_list
    if cn == 0:
        return 0

    board_len = 2**cn
    is_right, is_low = True, True
    if board_len // 2 > c:
        is_right = False
    if board_len // 2 > r:
        is_low = False

    temp = (board_len // 2)
    if not is_right and not is_low:
        return DQ(cn-1,r,c)
    elif is_right and not is_low:
        return blk_dist_list[cn-1] * 1 + DQ(cn-1,r,c - temp)
    elif not is_right and is_low:
        return blk_dist_list[cn-1] * 2 + DQ(cn-1,r - temp,c)
    elif is_right and is_low:
        return blk_dist_list[cn-1] * 3 + DQ(cn-1,r - temp,c - temp)

def main():
    global blk_dist_list
    n, r, c = map(int,input().split())
    blk_dist_list = list(range(n))
    for i in range(n):
        blk_dist_list[i] = (2**i) * (2**i)

    print(DQ(n,r,c))
    
if __name__ == "__main__":
    main()