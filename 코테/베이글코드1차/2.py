# 매번 subtree의 노드 수가 가장 많은 것의 연결을 끊기
from collections import defaultdict, deque

def dfs(n, info, graph, depth, level):
    if len(graph[n])==0:    # 리프노드
        level[depth].add(n)
        info[n] = 0
        return
    for child in graph[n]:
        dfs(child, info, graph, depth+1, level)
        info[n] += info[child] + 1
    level[depth].add(n)
    return

def solution(n, edges):
    answer = n
    graph = [[] for _ in range(n)]
    # level, # of subtree nodes
    info = [0 for _ in range(n)]
    level = defaultdict(set)
    unconnected = [False for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
    dfs(0, info, graph, 0, level)

    for i in range(1, len(level)):
        max_node_num = -1
        max_node_cnt = -1
        for node in level[i]:
            if unconnected[node]:   # 이미 차단된 노드
                continue
            if info[node] > max_node_cnt:
                max_node_cnt = info[node]
                max_node_num = node
        # 차단될 노드 선택됨
        q = deque([max_node_num])
        while q:
            now = q.popleft()
            for child in graph[now]:
                q.append(child)
                unconnected[child] = True
        print("level", i, ", select:", max_node_num, "removed_node_num:", info[max_node_num])
        if max_node_num == -1:
            return answer
        answer -= (info[max_node_num] + 1)
    return answer

    
print("answer:", solution(19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8],[3,9],[4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))
# 7
print("answer:", solution(14, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]]))
# 4
print("answer:", solution(10, [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3,9]]))
# 2


