sound = list(input())
# 5의 배수가 아니면 quack이 안됨
if len(sound) % 5 != 0:
    print(-1)
    exit()
quack = ['q', 'u', 'a', 'c', 'k']
visited = [False] * len(sound)
ans = 0
for i in range(len(sound)):
    if visited[i]:
        continue
    find = False
    if sound[i] == 'q': # quack 시작
        start = True
        idx = 1
        visited[i] = True
        for j in range(i+1, len(sound)):
            if sound[j] == quack[idx] and not visited[j]:
                visited[j] = True
                idx += 1
                if idx == 5:    # quack 완성
                    find = True
                    start = False
                    idx = 0 # 다시 q
        if find:
            ans += 1
        if start:   # 끝맺지 못한 quack이 있음
            print(-1)
            exit()
for i in range(len(visited)):
    if not visited[i]:
        print(-1)
        exit()
print(ans)