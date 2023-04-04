import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n = int(input())
parent = [i for i in range(1_000_001)]
parts = [1 for _ in range(1_000_001)]

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
        parts[a] += parts[b]
    else:
        parent[a] = b
        parts[b] += parts[a]

for _ in range(n):
    cmd = input()
    if cmd[0] == 'I':   # 부품 2개가 같은 로봇의 부품인지 알려줌
        i, a, b = cmd.split()
        a, b = map(int, [a, b])
        union(a, b)
    else:               # 로봇 c의 부품 몇 개?
        q, c = cmd.split()
        c = int(c)
        print(parts[find(c)])