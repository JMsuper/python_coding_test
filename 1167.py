# V <= 100,000 이기 때문에, 인접 리스트로 해결해야 한다.

import sys

input = sys.stdin.readline
print = sys.stdout.write

v_list = []
max_dist = 0
max_idx = 0

# 제일 긴 목적 노드의 idx, 거리 반환
def DFS(start,dist,visited):
    global v_list, max_dist, max_idx
    visited[start] = True
    for target_v, target_dist in v_list[start]:
        if visited[target_v] == False:
            if max_dist < dist + target_dist:
                max_dist = dist + target_dist
                max_idx = target_v
            DFS(target_v,dist+target_dist,visited)

def main():
    global v_list, max_idx, max_dist
    v = int(input().rstrip())
    v_list = list(range(v+1))
    for _ in range(1,v+1):
        input_list = list(map(int,input().rstrip().split()))
        cur_v = input_list[0]
        v_list[cur_v] = []
        for i in range(1,len(input_list)):
            if input_list[i] == -1 or i % 2 == 0:
                continue
            v_list[cur_v].append([input_list[i],input_list[i+1]])
    
    visited1 = [False for _ in range(v+1)]
    DFS(1,0,visited1)
    visited2 = [False for _ in range(v+1)]
    max_dist = 0
    DFS(max_idx,0,visited2)
    print(str(max_dist) + "\n")

if __name__ == "__main__":
    main()