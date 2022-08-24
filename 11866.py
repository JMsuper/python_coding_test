import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

def main():
    n, k = map(int,input().rstrip().split())
    circle = deque([])
    cur_pos = 0
    ans_list = []

    for i in range(n):
        circle.append(i+1)

    while len(circle) != 0:
        cur_pos = (cur_pos + k - 1) %  len(circle)
        ans_list.append(circle[cur_pos])
        circle.remove(circle[cur_pos])
    
    print("<")
    for i in range(len(ans_list)):
        print(str(ans_list[i]))
        if i < (len(ans_list) - 1):
            print(", ")
        else:
            print(">\n")
    

if __name__ == "__main__":
    main()