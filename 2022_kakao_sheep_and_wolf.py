def DFS(node, sheep, wolves, node_list):
    global global_info, max_sheep
    # print(node,sheep,wolves,node_list)
    if global_info[node] == 0:
        sheep += 1
        if sheep > max_sheep:
            max_sheep = sheep
    else:
        wolves += 1
    if wolves >= sheep:
        return
    
    for item in adj_list[node]:
        node_list.append(item)
    for new_node in node_list:
        DFS(new_node, sheep, wolves, [i for i in node_list if i != new_node])

def solution(info, edges):
    global global_info, adj_list, max_sheep
    global_info = info[:]
    answer = 0
    max_sheep = 0
    adj_list = [[] for _ in range(len(info) + 1)]
    for start, end in edges:
        adj_list[start].append(end)
    DFS(0,0,0,[])
    answer = max_sheep
    return answer

def main():
    info =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16]]
    print(solution(info,edges))

if __name__ == "__main__":
    main()