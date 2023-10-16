from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
people = list(input().split())
m = int(input())
graph = defaultdict(list)   # 후손 리스트 저장
indegree = defaultdict(int)  # 진입차수
for _ in range(m):
    x, y = input().split()  # x의 조상 y
    indegree[x] += 1
    graph[y].append(x)      # y의 후손 x

# 진입차수가 0인 노드 = 시조
q = deque()
for p in people:
    if indegree[p] == 0:
        q.append(p)
# 시조 출력
print(len(q))
print(*sorted(q))
family = {i: [] for i in people}  # 직접적인 부모-자식 관계
# 위상정렬
while q:
    now = q.popleft()
    for child in graph[now]:
        indegree[child] -= 1
        if indegree[child] == 0:
            family[now].append(child)
            q.append(child)
# 부모-자식 관계 출력
for parent, child in sorted(family.items()):
    print(parent, len(child), *sorted(child))
