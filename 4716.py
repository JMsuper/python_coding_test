# 입력의 마지막 줄에 0이 세 개 주어진다.
# 위 조건을 고려하지 않으면 33%에서 틀리게 된다.

def main():
    while 1:
        n, a, b = map(int,input().split())
        if n == 0 and a == 0 and b == 0:
            break
        cond_list = []
        ans = 0
        for _ in range(n):
            k,da,db = map(int,input().split())
            cond_list.append([k,da,db,abs(da-db)])

        cond_list.sort(key=lambda x:x[3],reverse=True)

        for k,da,db,_ in cond_list:
            room_cond = min(da,db)
            cnt = 0
            if room_cond == da:
                cnt = min(k,a)
                ans += cnt * da + (k - cnt) * db
                a -= cnt
                b -= k - cnt
            else:
                cnt = min(k,b)
                ans += (k - cnt) * da + cnt * db
                a -= k - cnt
                b -= cnt
        print(ans)


if __name__ == "__main__":
    main()