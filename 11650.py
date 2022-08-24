import sys

input = sys.stdin.readline
print = sys.stdout.write

def main():
    n = int(input().rstrip())
    n_list = []
    for _ in range(n):
        n_list.append(list(map(int,input().rstrip().split())))
    
    n_list.sort(key=lambda x : (x[0], x[1]))

    for item in n_list:
        print(str(item[0]) + " " + str(item[1]) + "\n")

if __name__ == "__main__":
    main()