n, m, k = map(int, input().split())
friend_fee = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    if a < b:
        parent[b] = a
        if friend_fee[a] > friend_fee[b]:
            friend_fee[a] = friend_fee[b]
    else:
        parent[a] = b
        if friend_fee[b] > friend_fee[a]:
            friend_fee[b] = friend_fee[a]
        
for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)
    
for i in range(1, n+1):
    parent[i] = find(i)

required_money = 0
for i in set(parent):
    required_money += friend_fee[i]

if k >= required_money:
    print(required_money)
else:
    print("Oh no")