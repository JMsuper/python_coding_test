def is_pellindrom(val):
    str_len = len(val)
    half_len = str_len // 2
    for i in range(half_len):
        if val[i] != val[str_len - 1 - i]:
            return "no"
    return "yes"

def main():
    while 1:
        num = input()
        if num == "0":
            break
        print(is_pellindrom(num))

if __name__ == "__main__":
    main()