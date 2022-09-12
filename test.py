
def convert_str_second(str_time):
    hour, minute, second = map(int,str_time.split(":"))
    return hour * 60 * 60 + minute * 60 + second 


def main():
    start = convert_str_second("01:30:59")
    end = convert_str_second("01:45:14")
    adv_time = convert_str_second("00:14:15")
    period_second = end - start
    print(start,end,adv_time,period_second)

if __name__ == "__main__":
    main()