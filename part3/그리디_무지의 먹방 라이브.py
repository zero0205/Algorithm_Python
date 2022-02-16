# # https://programmers.co.kr/learn/courses/30/lessons/42891

# def solution(food_times, k):
#     answer = 0
    
#     # food_times 모든 원소에 대해 k//len(food_times) 빼기
#     while k >= len(food_times):
#         rotation = k//len(food_times)    # 몫
#         k %= len(food_times)  # 나머지
#         for i in food_times:
#             i -= rotation
#             if i < 0:
#                 k += (-i)
#     answer = (k + 1) % len(food_times)
#     return answer

#### 답지 ####
import heapq

def solution(food_times, k):
    # 모두 먹는데 소요된 시간보다 네트워크 장애 발생 시간이 더 이후라면 -1 반환
    if sum(food_times) <= k:    
        return -1
        
    q = []    # 최소 힙을 저잦할 리스트
    
    # 최소 힙에 (소요 시간, 음식 번호) 넣음
    for idx in range(len(food_times)):
        heapq.heappush(q,(food_times[idx], idx + 1))  # (소요 시간, 음식 번호)
        
    sum_value = 0   # 먹기 위해 사용한 시간
    prev = 0        # 직전에 다 먹은 음식 시간
    length = len(food_times)    # 남은 음식의 개수
    while sum_value + ((q[0][0] - prev) - length) <= k:
        now = heapq.heappop(q)[0]   # 이번 턴에 다 먹을 음식의 소요 시간
        sum_value += (now - prev) * length 
        length -= 1 # 이번 턴에 다 먹은 음식 개수 빼줌
        prev = now  # 이전 음식 시간 재설정
        
    # 남은 음식 중 몇번째 음식인지 확인하여 출력
    answer = sorted(q, key=lambda x:x[1])
    return answer[(k - sum_value) % length][1]