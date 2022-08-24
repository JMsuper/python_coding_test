def is_triangle(line_list):
    line_list.sort()
    if (line_list[0]**2 + line_list[1]**2) == line_list[2]**2:
        return True
    else: return False


def main():
    while True:
        a, b, c = map(int,input().split())
        if a == b == c == 0:
            break
        if is_triangle([a,b,c]):
            print("right")
        else:
            print("wrong")

if __name__ == "__main__":
    main()