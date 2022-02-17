import heapq

def solution(n, weak, dist):
    answer = 0
    between = []
    prev = weak[0]
    for i in weak[1:]:
        # (사이 거리, 취약점1, 취약점2) 형태로 최소힙에 저장
        heapq.heappush(between, (i-prev, prev, i))  
        prev = i    # 이전 취약점 업데이트
    heapq.heappush(between, (n - prev +weak[0], prev, weak[0]))
    
    for j in len(dist):
        
    
    return answer