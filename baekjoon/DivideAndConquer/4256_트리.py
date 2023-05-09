import sys
input = sys.stdin.readline

def make_postorder(preorder, inorder):
    if len(preorder) == 1:  # 리프 노드
        return [preorder[0]]
    if len(preorder) == 0:  # 공집합
        return []
    root_idx = inorder.index(preorder[0])
    left = make_postorder(preorder[1:root_idx+1], inorder[:root_idx])
    right = make_postorder(preorder[root_idx+1:], inorder[root_idx+1:])
    return left+right+[preorder[0]]
            
for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    print(*make_postorder(preorder, inorder))