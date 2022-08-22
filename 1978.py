def is_prime_num(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def main():
    n = int(input())
    n_list = list(map(int,input().split()))
    ans = 0
    for item in n_list:
        if is_prime_num(item):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()