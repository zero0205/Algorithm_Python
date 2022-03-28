import heapq

def solution(abilities, k):
    answer = 0
    r = (len(abilities) + 1) // 2   # 라운드 수
    if len(abilities) % 2 == 1:
        abilities.append(0)
    abilities.sort(reverse=True)
    gap = []
    for i in range(r):
        heapq.heappush(gap,(-(abilities[2 * i] - abilities[2 * i + 1]), i))
    priority = [False] * r
    for j in range(k):
        temp = heapq.heappop(gap)
        priority[temp[1]] = True
    
    for idx in range(r):
        if priority[idx]:   # 우선권 사용 라운드
            answer += abilities[idx * 2]
        else:
            answer += abilities[idx * 2 + 1]
    return answer