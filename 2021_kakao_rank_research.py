import bisect

def solution(info, query):
    answer = []
    
    modified_info = []
    for item in info:
        lang, job, period, food, score = item.split()
        modified_info.append([lang,job,period,food,int(score)])
    
    modified_info.sort(key=lambda x:x[4])
    score_rank_list = [item[4] for item in modified_info]
    
    for item in query:
        query_item = item.split();
        
        lang = query_item[0]
        job = query_item[2]
        period = query_item[4]
        food = query_item[6]
        score = int(query_item[7])
        
        index = bisect.bisect_left(score_rank_list,score)
        
        cnt = 0
        for i in range(index,len(modified_info)):
            if lang != '-' and modified_info[i][0] != lang:
                continue
            if job != '-' and modified_info[i][1] != job:
                continue
            if period != '-' and modified_info[i][2] != period:
                continue
            if food != '-' and modified_info[i][3] != food:
                continue
            cnt += 1
        answer.append(cnt)

    return answer

def main():
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info,query))

if __name__ == "__main__":
    main()