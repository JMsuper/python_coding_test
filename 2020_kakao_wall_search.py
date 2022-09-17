def solution(n, weak, dist):
    dist.sort(reverse=True)
    weak_dict = {}
    for i in range(len(weak)):
        weak_dict[weak[i]] = i

    bit_weak = ""
    for _ in range(len(weak)):
        bit_weak += "0"
    bit_weak = int(bit_weak,2)

    target_bit = 2 ** len(weak) - 1

    prev_weak_list = set([0])
    cur_weak_list = []

    for dist_cnt in range(len(dist)):
        for item in prev_weak_list:
            wall_graph = []
            for i in range(len(weak_dict)):
                if item & (1 << i) == 0:
                    wall_graph.append(weak[i])
            wall_graph += [item + n for item in wall_graph]

            for i in range(len(wall_graph) // 2):
                new_bit_weak = item | (1 << weak_dict[wall_graph[i]])
                cur_dist = dist[dist_cnt]
                cur_idx = i
                while True:
                    distance = wall_graph[cur_idx+1] - wall_graph[cur_idx]
                    if distance <= cur_dist:
                        new_bit_weak = new_bit_weak | (1 << weak_dict[wall_graph[cur_idx+1] % n])
                        cur_dist = cur_dist - distance
                        cur_idx += 1
                    else:
                        cur_weak_list.append(new_bit_weak)
                        break
                if new_bit_weak == target_bit:
                    return dist_cnt
        prev_weak_list = set(cur_weak_list)
        cur_weak_list = []
    return -1

def main():
    n = 12
    weak = [1,5,6,10]
    dist = [1,2,3,4]
    print(solution(n,weak,dist))

if __name__ == "__main__":
    main()