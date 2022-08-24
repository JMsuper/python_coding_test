def get_room_num(info):
    h, w, n = info
    remain = n % h
    ret = n // h
    y = 0
    x = 0
    if remain == 0:
        y = ret
        x = h
    else:
        y = ret + 1
        x = remain
    ans = str(x)
    if y < 10:
        ans += "0" + str(y)
    else:
        ans += str(y)
    return ans
    


def main():
    # 걷는 거리가 같을 때, 아래 층 방을 더 선호
    t = int(input())
    t_list = []
    for _ in range(t):
        t_list.append(list(map(int,input().split())))
    for item in t_list:
        print(get_room_num(item))


if __name__ == "__main__":
    main()