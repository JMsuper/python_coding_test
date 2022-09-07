def solution(board, skill):
    answer = 0
    
    # 이 반복문들을 한번에 처리할 수 있는 방법이 없을까?
    # 보드에 접근하여 하나씩 수정해나가는 것은 비효율적

    # 동일한 영역을 다루는 스킬들에 대해 스킬을 분리하여
    # 통합하거 상쇄시키면 되지 않을까?
    clustered_skill = {}
    for t, r1, c1, r2, c2, degree in skill:
        if (r1,c1) in clustered_skill:
            clustered_skill[(r1,c1)].append([t,r1,c1,r2,c2,degree])
        else:
            clustered_skill[(r1,c1)] = [[t,r1,c1,r2,c2,degree]]
    print(clustered_skill)

    # # 이거 분할정복이다
    # for t, r1, c1, r2, c2, degree in skill:
    #     if t == 1:
    #         for i in range(r1,r2+1):
    #             for j in range(c1,c2+1):
    #                 board[i][j] -= degree
    #     else:
    #         for i in range(r1,r2+1):
    #             for j in range(c1,c2+1):
    #                 board[i][j] += degree
    
    
    
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if board[i][j] > 0:
    #             answer += 1
    return answer

def main():
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    solution(board,skill)

if __name__ == "__main__":
    main()