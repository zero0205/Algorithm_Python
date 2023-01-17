from collections import defaultdict
import heapq

def solution(k, tangerine):
    answer = 0
    # (귤사이즈 : 개수) 딕셔너리 
    t_num = defaultdict(int)
    for t in tangerine:
        t_num[t] += 1
        
    # (-크기별 귤의 개수, 귤의 크기)를 최소힙에 담기
    t_heap = []
    for key,value in t_num.items():
        heapq.heappush(t_heap, (-value, key))
    cnt = 0

    while True:
        num, size = heapq.heappop(t_heap)
        cnt += (-num)
        answer += 1
        # 개수 다 채우면 while문 탈출
        if cnt >= k:
            break
            
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
# 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
# 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
# 1