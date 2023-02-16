###################### 시간 초과 발생 풀이 ########################        
# from collections import deque
# import sys
# input = sys.stdin.readline
 
# n = int(input())    # 트리의 정점의 개수
# tree = [[] for _ in range(n+1)] # 트리
# bridge = []   # k번째 입력 간선
 
# for i in range(n-1):
#     a, b = map(int, input().split())
#     tree[a].append(b)
#     tree[b].append(a)
#     bridge.append((a,b))
 
# def bfs(node):
#     search_node_num = 1 # 방문한 노드 개수
    
#     q = deque([node])
#     visited = [False] * (n+1)
#     visited[node] = True    # 처음 노드 방문처리
    
#     while q:
#         now = q.popleft()
#         for nx in tree[now]:
#             if not visited[nx]:
#                 q.append(nx)
#                 visited[nx] = True
#                 search_node_num +=1
#     return search_node_num
    
# for _ in range(int(input())):   # 질의
#     # t == 1 : k번 정점이 단절점인지? (1 <= k <= n)
#     # t == 2 : k번째 간선이 단절선인지? (1 <= k <= n-1)
#     t, k = map(int, input().split())    
#     if t == 1:
#         flag = False
#         tmp = tree[k]
#         tree[k] = []
#         for node in tmp:
#             tree[node].remove(k)
#         for node in tmp:
#             if bfs(node) == n - 1:  # 그 노드만 없어지고 2개로 쪼개지지는 않음
#                 flag = True
#                 break
#         tree[k] = tmp
#         for node in tmp:
#             tree[node].append(k)
#         print("no" if flag else "yes")
#     else:
#         a, b = bridge[k-1]
#         tree[a].remove(b)
#         tree[b].remove(a)
#         if bfs(a) == n: # 간선 제거해도 다 연결되어 있는 경우
#             print("no")
#         else:           # 간선 제거하면 쪼개지는 경우
#             print("yes")
#         tree[a].append(b)
#         tree[b].append(a)
###################### 정답 풀이 ########################        
import sys
input = sys.stdin.readline

n = int(input())    # 트리의 정점의 개수
tree = [[] for _ in range(n+1)] # 트리

for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for _ in range(int(input())):   # 질의
    t, k = map(int, input().split())    
    if t == 1:  # k번 정점이 단절점인지? (1 <= k <= n)
        if len(tree[k]) == 1:   # k번 노드가 리프노드인 경우 => 단절점 X
            print("no")
        else:
            print("yes")
    else:       # k번째 간선이 단절선인지? (1 <= k <= n-1)
        print("yes")