fibo_result_list = [ - 1 for i in range(41)]

def fibonacci(n):
    if fibo_result_list[n] != -1:
        return fibo_result_list[n]
    if n == 0:
        fibo_result_list[0] = [1,0]
        return [1,0]
    elif n == 1:
        fibo_result_list[1] = [0,1]
        return [0,1]
    else:
        list1 = fibonacci(n-1)
        list2 = fibonacci(n-2)
        fibo_result_list[n] = [list1[0] + list2[0],list1[1] + list2[1]]
        return fibo_result_list[n]


def main():
    n = int(input())
    n_list = []
    for _ in range(n):
        n_list.append(int(input()))
    for item in n_list:
        cnt_0, cnt_1 = fibonacci(item)
        print(cnt_0,cnt_1)


if __name__ == "__main__":
    main()