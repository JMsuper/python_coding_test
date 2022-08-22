def merge_sort(arr):
    def sort(low,high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid,high)
        merge(low,mid,high)

    def merge(low,mid,high):
        result = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                result.append(arr[l])
                l += 1
            else:
                result.append(arr[h])
                h += 1
        while l < mid:
            result.append(arr[l])
            l += 1
        while h < high:
            result.append(arr[h])
            h += 1
    
        for i in range(low, high):
            arr[i] = result[i - low]
    
    sort(0, len(arr))
    return arr

def main():
    n = int(input())
    n_list = []
    for _ in range(n):
        n_list.append(int(input()))
    n_list = merge_sort(n_list)
    for item in n_list:
        print(item)

if __name__ == "__main__":
    main()