def mask(a, b):
    # 둘 다 매우 나쁨
    if a >= 151 and b >= 76:
        return 2
    # 둘 중 하나라도 나쁨
    elif a >=81 or b >= 36:
        return 1
    else:
        return 0

def solution(atmos):
    answer = 0
    used = 0
    for day in atmos:
        today = mask(day[0], day[1])
        # 쓰던 마스크 있는 경우
        if used > 0:
            used += 1
            if today == 2 or used > 3:  # 마스크 폐기
                used = 0
        # 쓰던 마스크 없는 경우
        else:
            if today > 0:   # 마스크 필요
                used = 1
                answer += 1
                if today == 2:
                    used = 0    # 마스크 폐기
    return answer

# 테스트 케이스
print(solution([[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]))
print(solution(([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]])))
print(solution([[30, 15], [80, 35]]))