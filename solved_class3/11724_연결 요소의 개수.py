# https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for idx in range(1, n + 1):
    for el in graph[idx]:
        union_parent(parent, idx, el)        
    
root = []
for el in parent[1:]:
    if el not in root:
        root.append(el)
    else:
        continue

print(len(root))