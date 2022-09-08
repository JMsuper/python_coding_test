# 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
# 단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
# 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
# 1명만 주문했던 메뉴는 제외

from itertools import combinations


def solution(orders, course):
    answer = []

    subject_list = []
    for cnt in course:
        cnt_dict = {}
        for order in orders:
            if len(order) < cnt:
                continue
            for subject in combinations(list(order),cnt):
                subject = list(subject)
                subject.sort()
                subject = tuple(subject)

                if subject in cnt_dict:
                    cnt_dict[subject] += 1
                else:
                    cnt_dict[subject] = 1
        for key, value in cnt_dict.items():
            if value >= 2:
                subject_list.append([key,value])
    subject_list.sort(key=lambda x:(len(x[0]),-x[1]))
    cur_len = 0
    cur_value = 0
    for subject in subject_list:
        if len(subject[0]) != cur_len: 
            cur_len = len(subject[0])
            cur_value = subject[1]
        if cur_len == len(subject[0]) and cur_value == subject[1]:
            answer.append(''.join(subject[0]))
            

    answer.sort()
    return answer

def main():
    orders = ["XYZ", "XWY", "WXA"]
    course = [2,3,4]
    print(solution(orders,course))

if __name__ == "__main__":
    main()