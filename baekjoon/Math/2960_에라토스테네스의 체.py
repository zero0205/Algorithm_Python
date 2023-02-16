n, k = map(int, input().split())

visited = [False] * (n+1)
cnt = 0
for i in range(2, n + 1):
    if visited[i]:   # 이미 지워진 수
        continue
    for j in range(i, n + 1, i):
        if not visited[j]:
            cnt += 1
            visited[j] = True    # 자기자신을 포함한 배수들 지우기
            if cnt == k:
                print(j)
                exit()