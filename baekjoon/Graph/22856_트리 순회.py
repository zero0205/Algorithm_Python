import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = 0

def inorder(node):
    global ans
    # 왼쪽 노드
    if tree[node][0] != -1 and not visited[tree[node][0]]:
        ans += 1
        inorder(tree[node][0])
    # 현재 노드 방문 처리
    visited[node] = True
    # 현재 노드가 유사 중위 순회의 끝인 경우
    if node == lastNode:
        print(ans)
        return
    # 오른쪽 노드
    if tree[node][1] != -1 and not visited[tree[node][1]]:
        ans += 1
        inorder(tree[node][1])
    ans += 1
        
for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a] = [b, c]

# 가장 마지막으로 방문하는 노드 찾기
now = 1
lastNode = 1
while True:
    if tree[now][1] == -1:
        lastNode = now
        break
    now = tree[now][1]
    
inorder(1)