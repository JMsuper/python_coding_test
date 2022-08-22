def main():
    n = int(input())
    str_list = []
    for _ in range(n):
        str_list.append(input())
    str_list = list(set(str_list))    
    str_list.sort(key=lambda x:(len(x),x))
    for item in str_list:
        print(item)

if __name__ == "__main__":
    main()