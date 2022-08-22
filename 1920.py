def binary_search(sorted_list, val):
    list_len = len(sorted_list)
    start = 0
    end = list_len - 1
    while 1:
        cur = (end + start) // 2
        if sorted_list[cur] == val:
            return True
        elif sorted_list[cur] > val:
            end = cur - 1
        else:
            start = cur + 1
        if end < start:
            break
    return False


def main():
    n = int(input())
    n_list = list(map(int,input().split()))
    n_list.sort()
    m = int(input())
    m_list = list(map(int,input().split()))
    for item in m_list:
        if binary_search(n_list,item):
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()