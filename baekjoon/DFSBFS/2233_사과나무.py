import sys
sys.setrecursionlimit(10**6)

n = int(input())
binary = '9' + input()
x, y = map(int, input().split())

parent = [[] for _ in range(n+1)]   # 각 노드의 부모(가까운 노드부터)
depth = [-1] * (n+1)  # 각 노드의 깊이
removed = []
inout = [[] for _ in range(n+1)]


def dfs(idx, stack, num):
    if idx >= len(binary):
        return
    if binary[idx] == '0':
        if stack:
            parent[num] = [stack[-1][1]]+parent[stack[-1][1]]
        depth[num] = len(stack)
        stack.append((idx, num))
        inout[num].append(idx)
        num += 1
    else:
        i, n = stack.pop()
        if idx == x or idx == y or i == x or i == y:
            removed.append(n)
        inout[n].append(idx)
    dfs(idx+1, stack, num)


dfs(1, [], 1)

if len(removed) == 1:
    print(*inout[removed[0]])
else:
    # LCA
    a, b = removed
    if depth[a] > depth[b]:
        a, b = b, a
    while depth[a] < depth[b]:
        b = parent[b][0]
    if a == b:
        print(*inout[a])
    else:
        for i in range(n):
            if parent[a][i] == parent[b][i]:
                print(*inout[parent[a][i]])
                break
