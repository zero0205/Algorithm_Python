from math import comb

n = int(input())
children = [0]*(n+1)
graph = []
for _ in range(n-1):
    u, v = map(int, input().split())
    children[u] += 1
    children[v] += 1
    graph.append((u, v))

d_num, g_num = 0, 0
# ㄷ
for u, v in graph:
    d_num += (children[u]-1)*(children[v]-1)

# ㅈ
for i in range(1, n+1):
    if children[i] >= 3:
        g_num += comb(children[i], 3)

if d_num > g_num*3:
    print("D")
elif d_num < g_num*3:
    print("G")
else:
    print("DUDUDUNGA")
