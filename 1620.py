
sorted_list = []
def get_idx_from_name(name):
    global sorted_list

    start = 0
    end = len(sorted_list) - 1
    pivot = len(sorted_list) // 2


    for _ in range(20):
        pivot = (start + end) // 2
        pivot_val = sorted_list[pivot][0]
        if pivot_val == name:
            return sorted_list[pivot][1]
        elif pivot_val < name:
            start = pivot + 1
            continue
        else:
            end = pivot - 1
            continue
    

def main():
    global sorted_list
    n, m = map(int,input().split())
    n_list = list(range(n))
    sorted_list = list(range(n))
    m_list = list(range(m))
    for i in range(n):
        val = input()
        n_list[i] = val
        sorted_list[i] = [val,i+1]
    for i in range(m):
        m_list[i] = input()
    
    sorted_list.sort(key=lambda x:x[0])

    for item in m_list:
        if item.isdigit():
            print(n_list[int(item)-1])
        else:
            print(get_idx_from_name(item))


    
if __name__ == "__main__":
    main()