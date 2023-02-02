n = int(input())
parent = list(map(int, input().split()))
delete_node = int(input())

tree = [[] for _ in range(n)]
root = -1
for i in range(n):
    if parent[i] != -1:
        tree[parent[i]].append(i)
    else:
        root = i
# print(tree)

def dfs(r):
    res = 0
    if not tree[r]:    # 리프 노드
        return 1
    for child in tree[r]:
        res += dfs(child)
    return res

# 노드 지우기
if parent[delete_node] != -1:   # 지우는 노드가 루트 노드가 아닐 때
    tree[parent[delete_node]].remove(delete_node)
    print(dfs(root))
else:                           # 지우는 노드가 루트 노드인 경우 => 다 없어짐
    print(0)