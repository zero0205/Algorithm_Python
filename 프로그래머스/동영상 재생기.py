# mm:ss => 초
def convertToSec(mmss):
    return int(mmss[:2])*60 + int(mmss[3:])

# 초 => mm:ss
def convertToMMSS(sec):
    mm = str(sec // 60).zfill(2)
    ss = str(sec%60).zfill(2)
    return mm+":"+ss

def solution(video_len, pos, op_start, op_end, commands):
    video_len = convertToSec(video_len)
    pos = convertToSec(pos)
    op_start = convertToSec(op_start)
    op_end = convertToSec(op_end)
    for cmd in commands:
        # 오프닝 구간인지 확인
        if op_start <= pos <= op_end:
            pos = op_end
        # 이동
        if cmd == "next":
            pos = min(pos+10, video_len)
        elif cmd == "prev":
            pos = max(pos-10, 0)
    # 오프닝 구간인지 확인
    if op_start <= pos <= op_end:
        pos = op_end
    answer = convertToMMSS(pos)
    return answer

solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"])