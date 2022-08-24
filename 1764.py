def main():
    n, m = map(int,input().split())
    n_list = list(range(n))
    for i in range(n):
        n_list[i] = input()
    m_list = list(range(m))
    for i in range(m):
        m_list[i] = input()
    n_set = set(n_list)
    m_set = set(m_list)
    ans_set = n_set.intersection(m_set)
    ans_list = list(ans_set)
    ans_list.sort()
    print(len(ans_list))
    for item in ans_list:
        print(item)

if __name__ == "__main__":
    main()