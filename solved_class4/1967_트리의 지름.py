# https://www.acmicpc.net/problem/1967

# import sys
# input = sys.stdin.readline

# n = int(input())
# tree = [[] for _ in range(n + 1)]
# length = [[] for _ in range(n + 1)]
# for _ in range(n - 1):
#     parent, child, cost = map(int, input().split())
#     tree[parent].append((child, cost))
    
# def dfs(start, l, visited, l_arr):
#     if not tree[start]:
#         l_arr.append(l)
#         return l_arr
#     else:
#         for n, c in tree[start]:
#             visited[n] = True
#             dfs(n, l + c, visited, l_arr)
#             visited[n] = False

# def get_length(root):
#     visited = [False] * (n + 1)
#     length[root].append(dfs(root, 0, visited, []))
#     if len(length[root]) >= 2:
#         length[root].sort()
#         return length[root][0] + length[root][1]
#     else:
#         return None

# max_value = -1  
# for i in range(1, n + 1):
#     # max_value = max(max_value, get_length(i))
#     print(get_length(i))

# # print(length)
# print(max_value)

#############################
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))
    
temp = [0, 0]
def bfs(start, n):
    q = deque([(start, 0)])
    visited = [False] * (n + 1)
    visited[start] = True
    while q:
        n, c = q.popleft()
        for next, cost in tree[n]:
            if not visited[next]:
                q.append((next, c + cost))
                visited[next] = True
                if temp[1] < c + cost:  # 더 긴 루트를 갖는다면
                    temp[0] = next
                    temp[1] = c + cost
    return temp

a = bfs(1, n)
b = bfs(a[0], n)   # 루트에서 가장 먼 노드에서 다시 bfs
print(b[1])