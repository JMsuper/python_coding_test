import itertools

def main():
    n, m = map(int,input().split())
    card_list = list(map(int,input().split()))
    nCr = itertools.combinations(card_list, 3)
    cur_abs = m
    cur_sum = 0
    for item in nCr:
        temp_sum = sum(item)
        if temp_sum <= m and cur_abs > (m - temp_sum):
            cur_sum = temp_sum
            cur_abs = m - temp_sum
    print(cur_sum)


if __name__ == "__main__":
    main()