# https://www.acmicpc.net/problem/1991

n = int(input())
graph = {}
for _ in range(n):
    parent, left, right = input().split()
    graph[parent] = (left, right)
    
parent = 'A'
def preorder(v, visited):
    if v not in visited:
        visited.append(v)
        if graph[v][0] != '.':
            preorder(graph[v][0], visited)
        if graph[v][1] != '.':
            preorder(graph[v][1], visited)
    return ''.join(visited)

def inorder(v, visited):
    if graph[v][0] != '.':
        inorder(graph[v][0], visited)
    if v not in visited:
        visited.append(v)
    if graph[v][1] != '.':
        inorder(graph[v][1], visited)
    return ''.join(visited)

def postorder(v, visited):
    if graph[v][0] != '.':
        postorder(graph[v][0], visited)
    if graph[v][1] != '.':
        postorder(graph[v][1], visited)
    if v not in visited:
        visited.append(v)
    return ''.join(visited)

visited = []
print(preorder(parent, visited))
visited = []
print(inorder(parent, visited))
visited = []
print(postorder(parent, visited))