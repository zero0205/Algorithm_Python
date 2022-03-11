def solution(N, stages):
    answer = []
    # (스테이지 도달했지만 클리어 못한 사람 수, 스테이지 도달 플레이어 수)
    clear_num = [0] * (N+2)
    stages.sort(reverse = True)
    
    for i in stages:
        clear_num[i] += 1   # 스테이지 도달했지만 클리어 못한 사람 수 체크
     
    accumulate = clear_num[N + 1]
    for n in range(N, 0, -1):
        accumulate += clear_num[n]
        if clear_num[n] != 0:
            failure = clear_num[n] / accumulate
        else:
            failure = 0
        answer.append((failure, n))
    
    answer.sort(key=lambda x : (-x[0], x[1]))
    return [y for x, y in answer]

n = int(input())
stages = list(map(int, input().split()))

print(solution(n, stages))

