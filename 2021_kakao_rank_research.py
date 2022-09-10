import bisect

def solution(info, query):
    answer = []
    info_dict = {}
    
    for lang in ["cpp","java","python","-"]:
        for job in ["backend","frontend","-"]:
            for period in ["junior","senior","-"]:
                for food in ["chicken","pizza","-"]:
                    info_dict[lang + job + period + food] = []
                    
    for item in info:
        item = item.split()
        for lang in [item[0],'-']:
            for job in [item[1],'-']:
                for period in [item[2],'-']:
                    for food in [item[3],'-']:
                        info_dict[lang + job + period + food].append(int(item[4]))
    
    for key, value in info_dict.items():
        value.sort()
        
    for item in query:
        item = item.replace(" and ","").split()
        query_q = item[0]
        query_score = int(item[1])
        
        idx = bisect.bisect_left(info_dict[query_q],query_score)
        cnt = len(info_dict[query_q]) - idx
        answer.append(cnt)

    return answer

def main():
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info,query))

if __name__ == "__main__":
    main()