

def init(rgb_list):
    temp_list = []
    temp_list.append(rgb_list[0][0] + rgb_list[1][1])
    temp_list.append(rgb_list[0][0] + rgb_list[1][2])
    temp_list.append(rgb_list[0][1] + rgb_list[1][0])
    temp_list.append(rgb_list[0][1] + rgb_list[1][2])
    temp_list.append(rgb_list[0][2] + rgb_list[1][0])
    temp_list.append(rgb_list[0][2] + rgb_list[1][1])

    ret_list = []
    ret_list.append(min([temp_list[2],temp_list[4]]))
    ret_list.append(min([temp_list[0],temp_list[5]]))
    ret_list.append(min([temp_list[1],temp_list[3]]))
    return ret_list

def main():
    n = int(input())
    rgb_list = []
    for _ in range(n):
        rgb_list.append(list(map(int,input().split())))

    ans = 0
    minimalized_list = init(rgb_list[0:2])
    if n > 2:
        for i in range(2,n):
            temp_list = []
            for j in range(3):
                min_val = 0
                if j == 0:
                    min_val = rgb_list[i][j] + min(minimalized_list[1],minimalized_list[2])
                elif j == 1:
                    min_val = rgb_list[i][j] + min(minimalized_list[0],minimalized_list[2])
                elif j == 2:
                    min_val = rgb_list[i][j] + min(minimalized_list[0],minimalized_list[1])
                temp_list.append(min_val)
            minimalized_list = temp_list
    ans = min(minimalized_list)
    print(ans)
    

if __name__ == "__main__":
    main()