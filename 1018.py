def find_paint_cnt(board, start_x, start_y):
    bw_cnt = [0,0]
    for color in range(2):
        if color == 0:
            prev = "W"
        else:
            prev = "B"
        cnt = 0
        for i in range(8):
            if i != 0:
                if prev == "B":
                    prev = "W"
                else:
                    prev = "B"
            for j in range(8):
                if board[start_x + i][start_y + j] == prev:
                    cnt += 1
                if prev == "B":
                    prev = "W"
                else:
                    prev = "B"
        bw_cnt[color] = cnt
    return min(bw_cnt) 


def main():
    m, n = map(int,input().split(' '))
    dm, dn = m - 7, n - 7
    ans = 65

    board = []
    for _ in range(m):
        board.append(list(input()))



    for i in range(dm):
        for j in range(dn):
            ans = min(ans,find_paint_cnt(board,i,j))
    print(ans)

if __name__ == "__main__":
    main()