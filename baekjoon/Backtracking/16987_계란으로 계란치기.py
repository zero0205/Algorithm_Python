n = int(input())
eggs = [[] for _ in range(n)]
for i in range(n):
    s, w = map(int, input().split())
    eggs[i].extend([s, w])

ans = 0    
def dfs(idx):
    global ans
    # 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란
    if idx == n:    
        res = 0
        for i in range(n):
            if eggs[i][0] <= 0:
                res += 1
        ans = max(ans, res)
        return
    # 본인이 깨진 계란인지
    if eggs[idx][0] <= 0:   
        dfs(idx+1)
        return
    # 본인 말고 다 깨졌는지 확인
    broken = True
    for i in range(n):
        if i == idx:
            continue
        if eggs[i][0] > 0:
            broken = False
    if broken:  # 깨지지 않은 다른 계란이 없음
        ans = max(ans, n-1)
        return
    # 계란 깨기
    for i in range(n):
        if i == idx:            # 본인
            continue
        if eggs[i][0] > 0:      # i번째 계란 치기 가능
            eggs[idx][0] -= eggs[i][1]  # 친 계란 내구도 감소
            eggs[i][0] -= eggs[idx][1]  # 치인 계란 내구도 감소
            dfs(idx+1)
            eggs[idx][0] += eggs[i][1]  # 친 계란 내구도 복구
            eggs[i][0] += eggs[idx][1]  # 치인 계란 내구도 복구

dfs(0)
print(ans)