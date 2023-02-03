import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
for _ in range(int(input())):
    t, k = map(int, input().split())
    if t == 1:  # 단절점인지?
        if len(tree[k]) == 1:   # 리프 노드일 때만 단절점이 아님
            print("no")
        else:
            print("yes")
    else:       # 단절선인지?
        print("yes")    # 트리에서는 모든 간선이 단절선