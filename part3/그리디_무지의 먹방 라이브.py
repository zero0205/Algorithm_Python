# https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    answer = 0
    
    # food_times 모든 원소에 대해 k//len(food_times) 빼기
    while k >= len(food_times):
        rotation = k//len(food_times)    # 몫
        k %= len(food_times)  # 나머지
        for i in food_times:
            i -= rotation
            if i < 0:
                k += (-i)
    answer = (k + 1) % len(food_times)
    return answer