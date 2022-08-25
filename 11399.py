import sys

input = sys.stdin.readline
print = sys.stdout.write

def main():
    n = int(input().rstrip())
    n_list = list(map(int,input().rstrip().split()))
    n_list.sort()
    ans = 0
    prev = 0
    for item in n_list:
        time = prev + item
        ans += time
        prev = time
    print(str(ans) + "\n")


if __name__ == "__main__":
    main()