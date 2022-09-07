import heapq

def solution(board, skill):
    answer = 0
    # 이거 분할정복이다

    # 스킬들이 한 행만 다루도록 자르기.
    # 즉, 스킬을 1차원으로 변경
    y_len = len(board[0])
    divided_skill = []
    for t, r1, c1, r2, c2, degree in skill:
        for i in range(r2-r1+1):
            start = (r1 + i) * y_len + c1
            end = (r1 + i) * y_len + c2
            if t == 1:
                heapq.heappush(divided_skill,[start,end,-degree])
            else:
                heapq.heappush(divided_skill,[start,end,degree])
    print(divided_skill)

    one_demension_skill = []
    # 겹치는 영역 합치거나 나누기
    while divided_skill:
        front = heapq.heappop(divided_skill)
        if not divided_skill:
            one_demension_skill.append(front)
            break
        if front[1] >= divided_skill[0][0]:
            back = heapq.heappop(divided_skill)
            if front[0] == back[0] and front[1] == back[1]:
                front[2] += back[2]
                heapq.heappush(divided_skill,front)
                continue
            elif front[0] == back[0]:
                front[2] += back[2]
                back[0] = front[1] + 1
                heapq.heappush(divided_skill,front)
                heapq.heappush(divided_skill,back)
                continue
            else:
                temp = [back[0],front[1],front[2]]
                front[1] = temp[0] - 1
                one_demension_skill.append(front)
                heapq.heappush(divided_skill,temp)
                heapq.heappush(divided_skill,back)
        else:
            one_demension_skill.append(front)

    print(one_demension_skill)
    for start, end, degree in one_demension_skill:
        x = start // y_len
        y_start = start % y_len
        y_end = end % y_len
        for i in range(y_start,y_end+1):
            board[x][i] += degree
    print(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer

def main():
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    print(solution(board,skill))

if __name__ == "__main__":
    main()