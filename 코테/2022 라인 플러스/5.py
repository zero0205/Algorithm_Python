import heapq

def solution(abilities, k):
    answer = 0
    r = (len(abilities) + 1) // 2   # 라운드 수
    if len(abilities) % 2 == 1:
        abilities.append(0)
    abilities.sort(reverse=True)    # 능력치 내림차순 정렬
    gap = []
    # 각 라운드마다 뽑을 수 있는 작은 값들의 합을 구해놓음
    # 그리고 각 라운드마다 능력치의 차이를 최대힙에 넣음
    for i in range(r):
        heapq.heappush(gap,-(abilities[2 * i] - abilities[2 * i + 1]))
        answer += abilities[2 * i + 1]
    # 능력치 차가 큰 라운드에서 우선권을 사용
    for _ in range(k):
        answer -= heapq.heappop(gap)    # 최대 힙 구현을 위해 -1 곱해서 넣었었어서 빼기로 해줌
    return answer

print(solution([2, 8, 3, 6, 1, 9, 1, 9], 2))
print(solution([7, 6, 8, 9, 10], 1))