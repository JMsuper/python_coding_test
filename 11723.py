import sys

input = sys.stdin.readline
print = sys.stdout.write

def main():
    m = int(input().rstrip())
    S = set([])
    for _ in range(m):
        cmd_list = input().rstrip().split()
        cmd = cmd_list[0]
        if cmd == "add":
            val = int(cmd_list[1])
            S.add(val)
            continue
        elif cmd == "remove":
            val = int(cmd_list[1])
            if val in S:
                S.remove(val)
            continue
        elif cmd == "check":
            val = int(cmd_list[1])
            if val in S:
                print("1\n")
            else:
                print("0\n")
            continue
        elif cmd == "toggle":
            val = int(cmd_list[1])
            if val in S:
                S.remove(val)
            else:
                S.add(val)
            continue
        elif cmd == "all":
            temp_S = []
            for i in range(1,21):
                temp_S.append(i)
            S = set(temp_S)
            continue
        elif cmd == "empty":
            S = set([])
            continue
        
if __name__ == "__main__":
    main()