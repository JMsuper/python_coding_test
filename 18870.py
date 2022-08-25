import sys

input = sys.stdin.readline
print = sys.stdout.write


def main():
    n = int(input().rstrip())
    n_list = list(map(int,input().rstrip().split()))
    temp_set = set(n_list)
    temp_list = list(temp_set)
    temp_list.sort()
    n_dict = {}
    for i in range(len(temp_set)):
        n_dict[temp_list[i]] = i
    for item in n_list:
        print(str(n_dict[item]) + " ")
    print("\n")

if __name__ == "__main__":
    main()