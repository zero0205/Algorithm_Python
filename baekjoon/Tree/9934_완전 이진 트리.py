# 중위 순회
k =  int(input())   # 트리의 깊이
input_data = list(map(int, input().split()))

tree = [[] for _ in range(k)]

def make_tree(sub_tree, depth):
    root = len(sub_tree)//2
    tree[depth].append(sub_tree[root]) # 현재 서브트리의 루트 tree 배열의 depth번째 배열에 저장
    
    if len(sub_tree) == 1:  # 리프노드인 경우
        return
    
    make_tree(sub_tree[:root], depth+1)     # 왼쪽 서브트리
    make_tree(sub_tree[root+1:], depth+1)   # 오른쪽 서브트리
    
make_tree(input_data, 0)

for t in tree:
    for node in t:
        print(node, end=' ')
    print()