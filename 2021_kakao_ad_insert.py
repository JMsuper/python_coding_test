def convert_str_second(str_time):
    hour, minute, second = map(int,str_time.split(":"))
    return hour * 60 * 60 + minute * 60 + second 

def convert_second_str(second_time):
    hour, minute, second = 0, 0, 0
    
    second = second_time % 60
    second_time //= 60
    minute = second_time % 60
    second_time //= 60
    hour = second_time

    if 9 >= hour >= 0:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    if 9 >= minute >= 0:
        minute = "0" + str(minute)
    else:
        minute = str(minute)
    if 9 >= second >= 0:
        second = "0" + str(second)
    else:
        second = str(second)
    return hour + ":" + minute + ":" + second

def solution(play_time, adv_time, logs):
    answer = ''

    adv_time_s = convert_str_second(adv_time)
    play_time_s = convert_str_second(play_time)
    
    time_list = [0 for _ in range(play_time_s + 1)]
    cum_time_list = [0 for _ in range(play_time_s)]
    
    # start 이상, end 미만
    for log in logs:
        start, end = map(convert_str_second,log.split("-"))
        time_list[start] += 1
        time_list[end] -= 1
    
    for i in range(1,len(time_list)):
        time_list[i] += time_list[i-1]

    
    for i in range(adv_time_s):
        cum_time_list[0] += time_list[i]
    
    start = 1
    while start + adv_time_s <= play_time_s:
        cum_time_list[start] = cum_time_list[start - 1] + time_list[start+adv_time_s-1] - time_list[start-1]
        start += 1
    
    max_val = max(cum_time_list)
    max_idx = 0
    for i in range(len(cum_time_list)):
        if cum_time_list[i] == max_val:
            max_idx = i
            break
    
    answer = convert_second_str(max_idx)
    
    return answer

def main():
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    print(solution(play_time,adv_time,logs))

if __name__ == "__main__":
    main()