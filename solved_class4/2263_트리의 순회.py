import sys
sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodePosition = [0] * (n + 1) 
for i in range(n):
    nodePosition[inorder[i]] = i

# postorder에서 마지막 원소가 그 트리의 루트 노드인 점을 이용
def preorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return 
    
    root = postorder[postEnd]   # postorder의 마지막 원소가 루트노드
    print(root, end=" ")
    
    left = nodePosition[root] - inStart # 왼쪽 서브트리 노드 수
    right = inEnd - nodePosition[root] # 오른쪽 서브트리 노드 수
    
    preorder(inStart, inStart + left - 1, postStart, postStart + left - 1)
    preorder(inEnd - right + 1, inEnd, postEnd - right, postEnd - 1)
    
preorder(0, n-1, 0, n-1)