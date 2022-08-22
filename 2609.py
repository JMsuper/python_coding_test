def gcd(a, b):
    prev = b
    remain = a % b
    while remain != 0:
        temp = remain
        remain = prev % remain
        prev = temp
    return prev


def main():
    a, b = map(int,input().split())
    max_prime = gcd(a,b)
    print(max_prime)
    print(int(a*b/max_prime))



if __name__ == "__main__":
    main()