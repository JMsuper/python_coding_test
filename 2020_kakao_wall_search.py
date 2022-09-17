def recursive(n,bit_weak,dist_cnt,dist_idx):
    # global global_dist, global_weak_dict, global_weak
    if dist_idx > dist_cnt:
        if bit_weak == 2**len(global_weak) - 1:
            return True
        else:
            return False

    wall_graph = []
    for i in range(len(global_weak_dict)):
        if bit_weak & (1 << i) == 0:
            wall_graph.append(global_weak[i])
    
    wall_graph += [item + n for item in wall_graph]

    for i in range(len(wall_graph) // 2):
        new_bit_weak = bit_weak | (1 << global_weak_dict[wall_graph[i]])
        cur_dist = global_dist[dist_idx]
        cur_idx = i
        while True:
            distance = wall_graph[cur_idx+1] - wall_graph[cur_idx]
            if distance <= cur_dist:
                # checked_weak.add(wall_graph[cur_idx+1] % n)
                new_bit_weak = new_bit_weak | (1 << global_weak_dict[wall_graph[cur_idx+1] % n])
                cur_dist = cur_dist - distance
                cur_idx += 1
            else:
                break

        if recursive(n,new_bit_weak,dist_cnt,dist_idx + 1):
            return True
    return False

def solution(n, weak, dist):
    global global_dist, global_weak, global_weak_dict
    answer = 0
    dist.sort(reverse=True)
    global_dist = dist
    global_weak = weak
    global_weak_dict = {}
    for i in range(len(weak)):
        global_weak_dict[weak[i]] = i

    bit_weak = ""
    for _ in range(len(weak)):
        bit_weak += "0"

    bit_weak = int(bit_weak,2)

    for dist_cnt in range(len(dist)):
        if recursive(n,bit_weak,dist_cnt,0):
            answer = dist_cnt + 1
            break
    if answer != 0:
        return answer
    else:
        return -1

def main():
    n = 12
    weak = [1,5,6,10]
    dist = [1,2,3,4]
    print(solution(n,weak,dist))

if __name__ == "__main__":
    main()