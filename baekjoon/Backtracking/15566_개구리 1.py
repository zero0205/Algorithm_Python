n, m = map(int, input().split())
# 각 개구리의 음식, 취미, 가족, 철학에 대한 흥미도
frogs = [[]]+[list(map(int, input().split())) for _ in range(n)]
# 개구리가 선호하는 연꽃의 번호
frog_prefers = [set()]+[set(map(int, input().split())) for _ in range(n)]
# 통나무 통로의 대화 주제
topics = [[-1]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    topics[a][b] = t
    topics[b][a] = t

lotus_frog = [-1]*(n+1)  # 각 연꽃에 사는 개구리 번호


def bt(idx):
    if idx > n:
        if check():
            print("YES")
            print(*lotus_frog[1:])
            exit()
        return
    for nx in frog_prefers[idx]:    # 연꽃 번호
        if lotus_frog[nx] == -1:    # 아직 아무도 차지하지 않았는지
            lotus_frog[nx] = idx
            bt(idx+1)
            lotus_frog[nx] = -1


def check():
    for i in range(1, n+1):  # 연꽃 번호 1
        for j in range(1, n+1):  # 연꽃 번호 2
            if topics[i][j] > 0:
                fa = lotus_frog[i]
                fb = lotus_frog[j]
                t = topics[i][j]
                if frogs[fa][t-1] != frogs[fb][t-1]:
                    return False
    return True


bt(1)
print("NO")
