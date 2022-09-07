def solution(board, skill):
    answer = 0

    # 누적합으로 해결한다.
    x_len = len(board)
    y_len = len(board[0])
    sum_board = [[0 for _ in range(y_len + 1)] for _ in range(x_len + 1)]

    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree = -degree
        sum_board[r1][c1] += degree
        sum_board[r2+1][c2+1] += degree
        sum_board[r1][c2+1] += -degree
        sum_board[r2+1][c1] += -degree

    for i in range(1,y_len+1):
        for j in range(0,x_len+1):
            sum_board[j][i] += sum_board[j][i-1]
    for i in range(1,x_len+1):
        for j in range(0,y_len+1):
            sum_board[i][j] += sum_board[i-1][j]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + sum_board[i][j] > 0:
                answer += 1
    return answer

def main():
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    print(solution(board,skill))

if __name__ == "__main__":
    main()