def solution(bakery_schedule, current_time, k):
    answer = 0
    ch, cm = map(int, current_time.split(":"))
    for i in range(len(bakery_schedule)):
        time, bbang = bakery_schedule[i].split()
        bh, bm = map(int, time.split(":"))
        if bh < ch: # 현재보다 이전 시간에 빵 나옴
            continue
        else:
            if bh == ch and bm < cm: # 현재보다 이전 시간에 빵 나옴
                continue
            else:
                answer += (60 * bh + bm) - (60 * ch + cm)
                k -= int(bbang)    
        if k <= 0:
            return answer
        ch, cm = bh, bm
    return -1

print(solution(["09:05 10", "12:20 5", "13:25 6", "14:24 5"], "12:05", 10))
# 80
print(solution(["12:00 10"], "12:00", 10))
# 0
print(solution(["12:00 10"], "12:00", 11))
# -1