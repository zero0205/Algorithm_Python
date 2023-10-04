from heapq import heappop, heappush

n, k = map(int, input().split())
height = list(map(int, input().split()))    # 오름차순 정렬된 원생들 키
# 인접한 원생끼리의 키 차이
diff = []
for i in range(1, n):
    heappush(diff, -(height[i]-height[i-1]))
# 경계선에 해당하는 값 제거
for _ in range(k-1):
    heappop(diff)

print(-sum(diff))
