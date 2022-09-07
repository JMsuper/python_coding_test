# 스킬을 사용하는 순서는 중요하지 않다.

# 스킬들을 조합하여 한번에 board에 적용하자
# 어떻게 스킬들을 조합?

def solution(board, skill):
    answer = 0
    
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    board[i][j] -= degree
        else:
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    board[i][j] += degree
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer