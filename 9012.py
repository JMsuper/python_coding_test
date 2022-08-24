def is_vps(str_val):
    stack = []
    for item in str_val:
        if item == "(":
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop(len(stack)-1)
    if len(stack) != 0:
        return False
    return True

def main():
    n = int(input())

    for _ in range(n):
        if is_vps(list(input())):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()