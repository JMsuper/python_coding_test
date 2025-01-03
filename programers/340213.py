# 문제 분석
# - 동영상 재생기 기능
#   1. 10초 전 이동 : prev
#     현재위치 < 10초 -> 현재위치를 0분 0초로 갱신
#   2. 10초 후 이동 : next
#     동영상 전체시간 - 현재위치 < 10 -> 현제위치를 영상의 마지막 위치로
#   3. 오프닝 건너뛰기
#     op_start <= 현재 재생 위치 <= op_end -> 자동으로 현재위치를 오프닝 끝나는 위치로
# - 변수 설명
#   - video_len : 동영상 길이(문자열)
#   - pos : 기능이 수행되기 직전의 재생위치(문자열)
#   - op_start : 오프닝 시작 시각(문자열)
#   - op_end : 오프닝 끝나는 시각(문자열)
#   - commands : 사용자 입력(1차원 문자열)
#   - return값 : "mm:ss" 문자열 <- 사용자 입력이 모두 끝난 후 동영상 위치
# - 제한사항 : 시간을 나타내는 요소는 모두 "mm:ss" 로 5글자
#   - 분, 초가 한 자리일 경우 -> 0붙여서 두 자리로
#   - 현재 위치 & op_end 은 동영상 범위 이내
#   - op_start < op_end
#
# 문제 풀이
# 1. 
def solution(video_len, pos, op_start, op_end, commands):
    n_video_len = str2num(video_len)
    n_pos = str2num(pos)
    n_op_start = str2num(op_start)
    n_op_end = str2num(op_end)
    
    n_pos = opening_pass(n_pos, n_op_start, n_op_end)
    
    for cmd in commands:
        if cmd == "prev":
            if n_pos < 10:
                n_pos = 0
            else:
                n_pos -= 10
        if cmd == "next":
            if n_video_len - n_pos < 10:
                n_pos = n_video_len
            else:
                n_pos += 10
        n_pos = opening_pass(n_pos, n_op_start, n_op_end)
    
    return num2str(n_pos)

def opening_pass(n_pos, n_op_start, n_op_end):
    if n_op_start <= n_pos <= n_op_end:
        return n_op_end
    return n_pos
    
def str2num(str):
    mm, ss = str.split(":")
    return int(mm) * 60 + int(ss)

def num2str(num):
    mm = num // 60
    ss = num % 60
    return num_format(mm) + ":" + num_format(ss)

def num_format(num):
    if num < 10:
        return "0" + str(num)
    return str(num)