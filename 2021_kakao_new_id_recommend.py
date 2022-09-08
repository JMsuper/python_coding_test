def solution(new_id):
    answer = ''

    possible_char_list = []
    for i in range(10):
        possible_char_list.append(str(i))
    for i in range(26):
        possible_char_list.append(chr(97+i))
    possible_char_list.append('-')
    possible_char_list.append('_')
    possible_char_list.append('.')
    
    # 1단계
    temp = ""
    for item in list(new_id):
        if item.isupper():
            temp += item.lower()
        else:
            temp += item
    new_id = temp

    # 2단계
    temp = ""
    for item in list(new_id):
        if item in possible_char_list:
            temp += item
    new_id = temp

    # 3단계
    temp = ""
    continuous_punctuation_cnt = 0
    for item in list(new_id):
        if item == '.':
            continuous_punctuation_cnt += 1
        elif continuous_punctuation_cnt > 0:
            temp += '.'
            continuous_punctuation_cnt = 0
            temp += item
        else:
            temp += item
    if continuous_punctuation_cnt > 0:
        temp += '.'
    new_id = temp

    # 4단계
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 5단계
    if new_id == '':
        new_id = "a"
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id[:14]
    
    # 7단계
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]

    answer = new_id
    
    return answer

def main():
    new_id = "=.="
    print(solution(new_id))

if __name__ == "__main__":
    main()