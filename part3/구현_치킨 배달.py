# import heapq

# # n : 도시 크기, m : 폐업할 치킨집 개수
# n, m = map(int, input().split())

# city = []   # 도시 정보 저장하는 배열
# for i in range(n):
#     city.append(list(map(int, input().split())))
    
# chicken = [(0,0)] * 14   # 치킨집은 최대 13개까지 존재. 인덱스가 치킨집 번호
# house = []
# chicken_distance = {}
# chicken_num = 1
# # 치킨집, 집 위치 파악
# for r in range(n):
#     for c in range(n):
#         if city[r][c] == 1: # 집
#             house.append((r+1,c+1))
#         elif city[r][c] == 2: # 치킨집
#             # chicken[n] : n번째 치킨집의 좌표
#             chicken[chicken_num] = (r + 1, c + 1)   
#             chicken_num += 1

# for h in house:
#     q = []  # 각 치킨집까지 치킨 거리를 담을 최소 힙
#     for c in chicken:
#         dist = abs(c[0] - h[0]) + abs(c[1] - h[1])
#         heapq.heappush(q, (dist, c[0],c[1]))
#     # n번째 집에서 각 치킨집까지의 거리 최소힙에 저장
#     chicken_distance[h] = q
    
# # q의 앞에서부터 m 빼버림
# for _ in range(len(q)-m):
#     heapq.heappop(q)

# answer = 0
# for j in q:
#     answer += j[0]
    
# print(answer)

############################################
# n : 도시 크기, m : 폐업할 치킨집 개수
import itertools

n, m = map(int, input().split())

city = []   # 도시 정보 저장하는 배열
# 도시 정보 입력받기
for i in range(n):
    city.append(list(map(int, input().split())))
    
chicken = []    # 치킨집 위치
house = []      # 집 위치

# 치킨집, 집 위치 파악
for r in range(n):
    for c in range(n):
        if city[r][c] == 1: # 집
            house.append((r+1,c+1))
        elif city[r][c] == 2: # 치킨집
            chicken.append((r+1,c+1))
            
answer = 10000000
# 도시의 치킨 거리 구하기
def get_chicken_disatnce(house, chicken):
    sum = 0
    for h in house:
        dist = 10000
        for c in chicken:
            # 최소 거리인 것만 남김
            dist = min(dist, abs(c[0] - h[0]) + abs(c[1] - h[1]))
        sum += dist    
    return sum  # 도시의 치킨 거리 반환    

# 치킨집 중 m개 고르기 (조합 사용)
selected_chicken = itertools.combinations(chicken, m)

for el in selected_chicken:
    answer = min(answer, get_chicken_disatnce(house, selected_chicken))
    
print(answer)