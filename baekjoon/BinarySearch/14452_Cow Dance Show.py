from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, t_max = map(int, input().split())
durations = [int(input()) for _ in range(n)]


def calculate_total_duration(k):
    stage = []
    # 시작
    for i in range(k):
        heappush(stage, durations[i])

    # 무대 진행
    time = 0
    d_idx = k
    while time <= t_max:
        # 공연 다 한 소 내려와
        while stage and stage[0] == time:
            heappop(stage)
        # 자리 남았으면 소 올라가
        while len(stage) < k and d_idx < n:
            heappush(stage, time+durations[d_idx])
            d_idx += 1
        # 소들 공연 끝났으면 그 때의 시간 리턴
        if len(stage) == 0:
            return time
        time += 1
    # t_max 내로 공연을 못 마친 경우
    return t_max+1


left, right = 1, n
while left <= right:
    k = (left+right)//2
    needed_time = calculate_total_duration(k)
    if needed_time <= t_max:
        right = k-1
    else:
        left = k+1
print(right+1)
