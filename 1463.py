num_list = []

def DP(cnt,val,state):
    global num_list
    if val == 1:
        num_list[1] = min(cnt,num_list[1])
        return
    if num_list[val] > cnt:
        num_list[val] = cnt
    else:
        return
    
    if val % 3 == 0:
        DP(cnt + 1, val // 3,"3")
    if val % 2 == 0:
        DP(cnt + 1, val // 2,"2")
    if state == "minus":
        DP(cnt + 1, val - 1,"doubleminus")
    elif state == "doubleminus":
        return
    else:
        DP(cnt + 1, val - 1,"minus")
    

def main():
    global num_list
    n = int(input())
    num_list = [ 1000000 for _ in range(1000001)]
    DP(0,n,"")
    print(num_list[1])
    
if __name__ == "__main__":
    main()