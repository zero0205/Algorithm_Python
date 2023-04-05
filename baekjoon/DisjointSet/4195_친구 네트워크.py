import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent, friend):
    a = find(a, parent)
    b = find(b, parent)
    
    if a == b:
        return
    if a < b:
        parent[b] = a
        friend[a] += friend[b]
    else:
        parent[a] = b 
        friend[b] += friend[a]
        
for _ in range(int(input())):
    f = int(input())
    parent = dict()
    friend = dict()
    for _ in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            friend[a] = 1
        if b not in parent:
            parent[b] = b
            friend[b] = 1
        union(a, b, parent, friend)
        print(friend[find(a, parent)])