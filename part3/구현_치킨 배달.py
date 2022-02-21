# n : 도시 크기, m : 남을 치킨집 개수
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
    for hx, hy in house:
        dist = 10000
        for cx, cy in chicken:
            # 최소 거리인 것만 남김
            dist = min(dist, abs(cx - hx) + abs(cy - hy))
        sum += dist    
    return sum  # 도시의 치킨 거리 반환    

# 치킨집 중 m개 고르기 (조합 사용)
selected_chicken = list(itertools.combinations(chicken, m))

for el in selected_chicken:
    answer = min(answer, get_chicken_disatnce(house, el))
    
print(answer)