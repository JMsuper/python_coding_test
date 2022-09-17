


def recursive(n,weak,dist_cnt,dist_idx):
    global global_dist
    if dist_idx > dist_cnt:
        if len(weak) > 0:
            return False
        else:
            return True

    wall_graph = weak + [item + n for item in weak]

    for i in range(len(weak)):
        checked_weak = set([weak[i]])
        cur_dist = global_dist[dist_idx]
        cur_idx = i
        while True:
            distance = wall_graph[cur_idx+1] - wall_graph[cur_idx]
            if distance <= cur_dist:
                checked_weak.add(wall_graph[cur_idx+1] % n)
                cur_dist = cur_dist - distance
                cur_idx += 1
            else:
                break
        new_weak = list(set(weak) - checked_weak)
        new_weak.sort()
        if recursive(n,new_weak,dist_cnt,dist_idx + 1):
            return True
    return False

def solution(n, weak, dist):
    global global_dist
    answer = 0
    dist.sort(reverse=True)
    global_dist = dist

    for dist_cnt in range(len(dist)):
        if recursive(n,weak,dist_cnt,0):
            answer = dist_cnt + 1
            break
    if answer != 0:
        return answer
    else:
        return -1

def main():
    n = 12
    weak = [1,3,4,9,10]
    dist = [3,5,7]
    print(solution(n,weak,dist))

if __name__ == "__main__":
    main()