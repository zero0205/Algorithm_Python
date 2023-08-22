from itertools import permutations

n, k = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    input_data = list(map(int, input().split()))
    for j in range(1, n+1):
        arr[i][j] = input_data[j-1]
kh = list(map(int, input().split()))
mh = list(map(int, input().split()))


def dfs(p1, p2, idx, rsp, win):
    if win[0] == k:  # 지우 우승
        return True
    if win[1] == k or win[2] == k:    # 민호 또는 경희 우승
        return False
    if idx[0] == n:  # 지우가 모든 손동작을 사용해도 우승자가 안 나옴
        return False

    if p1 > p2:
        p1, p2 = p2, p1
    p3 = 3 - (p1 + p2)  # 이번 경기에 참여하지 않은 사람

    if arr[rsp[p1][idx[p1]]][rsp[p2][idx[p2]]] == 2:    # p1 승
        win[p1] += 1
        idx[p1] += 1
        idx[p2] += 1
        return dfs(p1, p3, idx, rsp, win)
    else:   # p2 승
        win[p2] += 1
        idx[p1] += 1
        idx[p2] += 1
        return dfs(p2, p3, idx, rsp, win)


for jw in permutations(range(1, n+1)):
    rsp = [list(jw), kh, mh]    # 손동작 순서 배열
    idx = [0] * 3   # 각 참여자들이 낼 손동작 배열의 인덱스
    win = [0] * 3   # 각 참여자들이 이긴 횟수
    if dfs(0, 1, idx, rsp, win):
        print(1)
        exit()
print(0)
