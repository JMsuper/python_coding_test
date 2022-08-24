from math import factorial

def main():
    n, k = map(int,input().split())
    print(int(factorial(n) / (factorial(n - k) * factorial(k))))


if __name__ == "__main__":
    main()