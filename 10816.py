import bisect


def count_num_in_list(val,m_list):
    left = bisect.bisect_left(m_list,val)
    right = bisect.bisect_right(m_list,val)
    return right - left

def main():
    n = int(input())
    n_list = list(map(int,input().split()))
    m = int(input())
    m_list = list(map(int,input().split()))

    ans_list = []

    n_list.sort()
    for item in m_list:
        ans_list.append(count_num_in_list(item,n_list))

    for ans in ans_list:
        print(ans,end=" ")


if __name__ == "__main__":
    main()