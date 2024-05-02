from heapq import heappop, heappush

n = int(input())
time = []
for _ in range(n):
    s, e = map(int, input().split())
    time.append((s, e))
time.sort()  # 시작 시간을 기준으로 오름차순 정렬

hq = []  # 우선순위 큐 => 사용 중인 회의실들의 사용 종료 시각
for i in range(n):
    if hq and hq[0] <= time[i][0]:  # 지금 사용할 수 있는 회의실이 있다면
        heappop(hq)
    heappush(hq, time[i][1])
print(len(hq))
