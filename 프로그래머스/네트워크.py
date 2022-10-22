# def find(parent, x):
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])
#     return parent[x]

# def union(parent, a, b):
#     a = find(parent, a)
#     b = find(parent, b)
    
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def solution(n, computers):
#     answer = 0
#     parent = [i for i in range(n)]
#     for i in range(n):
#         for j in range(i, n):
#             if i == j:
#                 continue
#             else:
#                 if computers[i][j] == 1:
#                     union(parent, i, j)
#     return len(set(parent))