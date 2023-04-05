import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

parent = [i for i in range(g+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
        
# 비행기는 입력으로 받은 수보다 같거나 작은 번호의 게이트에 도킹해야함
planes = []
for _ in range(p):
    planes.append(int(input()))

ans = 0
for plane in planes:
    docking_gate = find(plane)
    if docking_gate == 0:   # 도킹할 수 있는 gi보다 작거나 같은 번호의 게이트가 없음
        break
    parent[docking_gate] = parent[docking_gate-1]
    ans += 1
print(ans)