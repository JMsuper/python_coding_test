def main():
    n = int(input())
    info_list = []
    for i in range(n):
        age, name = input().split()
        info_list.append([int(age),name,i])
    info_list.sort(key=lambda x : (x[0],x[2]))
    for item in info_list:
        print(item[0],item[1])


if __name__ == "__main__":
    main()