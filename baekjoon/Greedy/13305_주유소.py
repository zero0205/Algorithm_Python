############### 부분 성공 ######################
# import sys, heapq
# input = sys.stdin.readline

# n = int(input())    # 도시의 개수
# road = list(map(int, input().split()))  # 인접한 두 도시를 연결하는 도로의 길이
# cost = list(map(int, input().split()))  # N번째 도시의 주유소 리터당 가격

# cost_sort = []
# for i in range(len(cost) - 1):
#     heapq.heappush(cost_sort, (cost[i], -i))

# ans = 0
# idx = n - 1
# while True:
#     c, i = heapq.heappop(cost_sort)
#     i = -i
#     if i == 0:
#         ans += c * road[0]
#         break
#     if i > idx:     # 이미 전에 채워옴
#         continue
#     else:
#         for j in range(i, idx):
#             ans += c * road[j]
#         idx = i
# print(ans)

###############################################
import sys
input = sys.stdin.readline

n = int(input())    # 도시의 개수
road = list(map(int, input().split()))  # 인접한 두 도시를 연결하는 도로의 길이
cost = list(map(int, input().split()))  # N번째 도시의 주유소 리터당 가격

now_cost = cost[0]
ans = now_cost * road[0]
for i in range(1, n-1):
    if now_cost > cost[i]:  # 이전보다 싼 주유소 등장
        now_cost = cost[i]
    ans += now_cost * road[i]

print(ans)