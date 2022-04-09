# https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# graph = [[(i,i,i)] for i in range(10001)]   # 부모, 왼쪽자식, 오른쪽자식

# prev = int(input())
# while True:
#     now = int(input())
#     if now < prev:  # 왼쪽 자식
#         graph[prev][1] = now
#         graph[now][0] = prev
#         continue
#     else:
#         while graph[prev][1] != prev: # 이미 방문한 노드
#             prev = graph[prev][0]
#         graph[prev][2] = now
pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break
    
def post_order(start, end):
    if start > end:
        return
    
    root = pre_order[start] # 루트 노드
    idx = start + 1
    
    # 루트보다 커지는 지점을 찾기
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1
        
    post_order(start + 1, idx -1)   # 왼쪽 서브트리
    post_order(idx, end)    # 오른쪽 서브트리
    
    print(root)
    
post_order(0, len(pre_order) - 1)