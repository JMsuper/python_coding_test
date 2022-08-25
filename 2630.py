import math
import sys

input = sys.stdin.readline
print = sys.stdout.write
board = []
dx = [0,0,1,1]
dy = [0,1,0,1]
ans_w, ans_b = 0, 0

def get_state(x,y,length):
    global board
    cur_color = board[x][y]
    for i in range(length):
        for j in range(length):
            temp_color = board[x+i][y+j]
            if temp_color != cur_color:
                return "mixed"
    if cur_color == 0:
        return "white"
    else:
        return "blue"

def recursive(x,y,length):
    global ans_w, ans_b

    for i in range(4):
        cx, cy = x + dx[i] * length//2, y + dy[i] * length//2
        state = get_state(cx,cy,length//2)
        if state == "mixed":
            recursive(cx,cy,length//2)
        elif state == "white":
            ans_w += 1
        elif state == "blue":
            ans_b += 1

def main():
    global board, ans_w, ans_b
    n = int(input().rstrip())
    board = []
    for _ in range(n):
        board.append(list(map(int,input().rstrip().split())))
    state = get_state(0,0,n)
    if state == "mixed": 
        recursive(0,0,n)
        print(str(ans_w) + "\n")
        print(str(ans_b) + "\n")
    elif state == "white":
        print("1\n")
        print("0\n")
    else:
        print("0\n")
        print("1\n")


if __name__ == "__main__":
    main()