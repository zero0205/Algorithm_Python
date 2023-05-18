import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
# 건물 관계
relation = [[] for _ in range(n+1)]
indegree = [0] * (n+1)  # i번째 건물을 짓기 위해 선행되어야 하는 건물 수
for _ in range(m):
    x, y  = map(int, input().split())
    relation[x].append(y)   # x를 건설해야 y 건설 가능
    indegree[y] += 1
    
# 영우의 게임 정보
building = [0] * (n+1)  # i번째 빌딩 개수
for _ in range(k):
    a, b = map(int, input().split())
    if a == 1:  # 건설
        if indegree[b] > 0:    # 선행되어야 하는 건물이 모두 건설되지 않았는데 건설
            print("Lier!")
            exit()
        building[b] += 1
        if building[b] == 1:    # b번 빌딩이 없다가 지어진 경우
            for nx in relation[b]:  # 다음 건물들 진입 차수 감소
                indegree[nx] -= 1
    else:   # 파괴
        if building[b] <= 0:    # 건설 정보에 없는 건물 파괴
            print("Lier!")
            exit()
        building[b] -= 1
        if building[b] == 0:    # 건물 파괴하니 하나도 없는 경우
            for nx in relation[b]:
                indegree[nx] += 1
        
print("King-God-Emperor")