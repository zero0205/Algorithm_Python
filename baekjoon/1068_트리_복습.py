n = int(input())
parent = list(map(int, input().split()))
delete_node = int(input())
ans = 0
tree = [[] for _ in range(n)]
for i in range(n):
    if parent[i] != -1:
        tree[parent[i]].append(i)   # 부모 -> 자식 표시
    else:
        root = i
    
def dfs(root):
    ans = 0
    if len(tree[root]) == 0:  # 리프 노드라면
        return 1 
    for child in tree[root]:
        ans += dfs(child)
    return ans

if delete_node == root: # 지우는 노드가 루트라면 다 없어짐
    print(0)
else:
    tree[parent[delete_node]].remove(delete_node)
    print(dfs(root))