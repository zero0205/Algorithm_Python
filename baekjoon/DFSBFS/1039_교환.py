from collections import deque, defaultdict

n, k = input().split()
n_len = len(n)
k = int(k)

q = deque([(n, 0)])
visited = defaultdict(set)
visited[n].add(0)
answer = -1
while q:
    now, cnt = q.popleft()
    if cnt == k:
        answer = max(int(now), answer)
        continue
    for i in range(n_len-1):
        for j in range(i+1, n_len):
            if (i == 0 and now[j] == '0'):
                continue
            new_num = now[:i]+now[j]+now[i+1:j]+now[i]+now[j+1:]
            if (new_num not in visited or cnt+1 not in visited[new_num]) and cnt < k:
                q.append((new_num, cnt+1))
                visited[new_num].add(cnt+1)
print(answer)
