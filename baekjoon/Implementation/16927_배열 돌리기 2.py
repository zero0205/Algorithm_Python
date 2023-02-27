from collections import deque

n, m, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
for cnt in range(min(n, m)//2):
    top_r, top_c = cnt, cnt   # 왼위
    bottom_r, bottom_c = n-1-cnt, m-1-cnt   # 오른아래
    q = deque([])
    # 왼줄
    for i in range(top_r, bottom_r):
        q.append(arr[i][top_c])
    # 아랫줄
    for i in range(top_c, bottom_c):
        q.append(arr[bottom_r][i])
    # 오른줄
    for i in range(bottom_r, top_r, -1):
        q.append(arr[i][bottom_c])
    # 윗줄
    for i in range(bottom_c, top_c, -1):
        q.append(arr[top_r][i])
    
    q.rotate(r)
    
    # 왼줄
    for i in range(top_r, bottom_r):
        arr[i][top_c] = q.popleft()
    # 아랫줄
    for i in range(top_c, bottom_c):
        arr[bottom_r][i] = q.popleft()
    # 오른줄
    for i in range(bottom_r, top_r, -1):
        arr[i][bottom_c] = q.popleft()
    # 윗줄
    for i in range(bottom_c, top_c, -1):
        arr[top_r][i] = q.popleft()
    
for r in arr:
    print(*r)