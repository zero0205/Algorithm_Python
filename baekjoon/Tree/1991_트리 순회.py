def preorder(tree, node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree, tree[node][0])
    preorder(tree, tree[node][1])
    
def inorder(tree, node):
    if node == '.':
        return
    inorder(tree, tree[node][0])
    print(node, end='')
    inorder(tree, tree[node][1])
    
def postorder(tree, node):
    if node == '.':
        return
    postorder(tree, tree[node][0])
    postorder(tree, tree[node][1])
    print(node, end='')

n = int(input())
tree = dict()
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = [left, right]
    
preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')