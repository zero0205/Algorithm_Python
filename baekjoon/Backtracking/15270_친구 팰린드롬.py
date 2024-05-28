n, m = map(int, input().split())
friends = []
for _ in range(m):
    u, v = map(int, input().split())
    friends.append((u, v))
ans = 0


def bt(used, idx):
    global ans
    if idx == m:
        if len(used) < n:
            ans = max(ans, len(used)+1)
        else:
            print(n)
            exit()
        return
    # idx번째 참가
    if friends[idx][0] not in used and friends[idx][1] not in used:
        used.add(friends[idx][0])
        used.add(friends[idx][1])
        bt(used, idx+1)
        used.remove(friends[idx][0])
        used.remove(friends[idx][1])
    # idx번째 참가 X
    bt(used, idx+1)


bt(set(), 0)
print(ans)
