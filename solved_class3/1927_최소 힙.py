# # https://www.acmicpc.net/problem/1927

# import heapq
# import sys
# input = sys.stdin.readline

# n = int(input())

# q = []

# for _ in range(n):
#     num = int(input())
#     if num == 0:    # 배열에서 가장 작은 값 pop
#         if len(q) == 0:
#             print(0)
#         else:
#             print(heapq.heappop(q))
#     else:
#         heapq.heappush(q, num)
        
########### 최소힙 구현 ################
# def insert(tree, value):
#     # 트리의 맨 뒤에 삽입
#     tree.append(value)
    
#     parent = len(tree) - 1  # 부모 노드
#     child = parent          # 자식 노드
    
#     while parent > 1:
#         # 부모 노드의 인덱스는 자식 노드 인덱스 // 2
#         parent //= 2
#         # 부모와 비교하여 부모보다 작으면 자리 바꿔줌        
#         if tree[parent] > value:
#             tree[child] = tree[parent]
#             child = parent
#         else:
#             break
#     # 현재 자식 노드 위치에 값 넣어주기
#     tree[child] = value
#     return

# def get_priority(tree, node):
#     if len(tree) - 1 >= node * 2 + 1:  # 자식 노드 둘 다 있음
#         # 작은 값을 갖는 노드의 번호 리턴
#         if tree[node * 2] > tree[node * 2 + 1]:
#             return node * 2 + 1 
#         else:
#             return node * 2
#     elif len(tree) - 1 == node * 2: # 왼쪽 자식 노드만 존재
#         return node * 2
#     else:
#         return -1
# def delete(tree):
#     if len(tree) == 1:
#         return 0
    
#     return_value = tree[1]
#     last_data = tree[-1]
#     node = 1
    
#     while True:
#         # 자식 노드 중 작은 값을 갖는 노드 찾기
#         pri_node = get_priority(tree, node)
        
#         if pri_node == -1:  # 자식 노드 없음
#             break
#         # 자식 노드 있고, 나보다 그 값이 작음
#         if last_data > tree[pri_node]:
#             tree[node] = tree[pri_node]
#             node = pri_node
#         else:
#             break
#     # 현재 노드에 값 저장
#     tree[node] = last_data
#     tree.pop()
#     return return_value         

# n = int(input())
# tree = [0]
# for _ in range(n):
#     num = int(input())
#     if num == 0:    # pop 연산
#         print(delete(tree))
#     else:
#         insert(tree, num)