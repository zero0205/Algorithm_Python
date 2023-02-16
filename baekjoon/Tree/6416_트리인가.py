from collections import defaultdict

def chk_tree(tree, node):
    root = 0
    for v, u in tree.items():
        if len(tree[v]) > 0: # 한 노드로 들어오는 간선이 2개 이상인 경우 트리 X
            return False
        # 루트 노드 찾기
        now = v
        while True:
            if root != 0 and 
    return True   
            
            
t = 1
while True:
    line = list(map(int, input().split()))
    
    # 입력 종료 조건
    if len(line) == 2 and line[0] < 0 and line[1] < 0:
        break
    
    tree = defaultdict(list)
    node = set()
    for i in range(0, len(line), 2):
        u, v = line[i], line[i+1]
        # 테스트 케이스 종료
        if u == 0 and v == 0:
            # 트리인지 확인
            if chk_tree(tree, node):
                print("Case", t, "is a tree")
            else:
                print("Case", t, "is not a tree")
            # 트리 clear
            tree.clear()
            t += 1
            continue
        
        # tree에 들어오는 간선의 출발점 노드 번호를 저장
        tree[v].append(u)
        # node 집합에 노드들 저장
        node.add(u)
        node.add(v)
        