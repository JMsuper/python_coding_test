def solution(video_len: str, pos: str, op_start: str, op_end: str, commands: list[str]) -> str:
    # 모든 시간을 초 단위로 변환
    total_seconds = str2seconds(video_len)
    current_pos = str2seconds(pos)
    opening_start = str2seconds(op_start)
    opening_end = str2seconds(op_end)
    
    current_pos = skip_opening(current_pos, opening_start, opening_end)
    
    for command in commands:
        if command == "prev":
            current_pos = max(0, current_pos - 10)
        elif command == "next":
            current_pos = min(total_seconds, current_pos + 10)
            
        current_pos = skip_opening(current_pos, opening_start, opening_end)
    
    return seconds2str(current_pos)

def skip_opening(position: int, start: int, end: int) -> int:
    """오프닝 구간에 있다면 끝 지점으로 이동"""
    return end if start <= position <= end else position
    
def str2seconds(time_str: str) -> int:
    """mm:ss 형식의 시간 문자열을 초 단위로 변환"""
    minutes, seconds = map(int, time_str.split(":"))
    return minutes * 60 + seconds

def seconds2str(seconds: int) -> str:
    """초 단위 시간을 mm:ss 형식 문자열로 변환"""
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes:02d}:{remaining_seconds:02d}"