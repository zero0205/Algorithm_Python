import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        # 가장 맵지 않은 음식의 스코빌 지수가 k가 되면 break
        if scoville[0] >= K:
            break
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        mapzzil = heapq.heappop(scoville)
        mapzzil2 = heapq.heappop(scoville)
        heapq.heappush(scoville, mapzzil+mapzzil2*2)
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
# 2