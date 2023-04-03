import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
graph = defaultdict(set)
propositions = set()    # 등장한 명제들

for _ in range(n):
    p, _, q = input().split()
    if p == q:  # 전건과 후건이 같은 경우
        continue
    propositions.add(p)
    propositions.add(q)
    graph[p].add(q)

# 플로이드-워셜
for k in propositions:
    for i in propositions:
        for j in propositions:
            if i == j:
                continue
            if (k in graph[i]) and (j in graph[k]):
                graph[i].add(j)
ans = []
for key in sorted(graph):
    for v in sorted(graph[key]):
        if key != v:
            ans.append(key + " => " + v)            
print(len(ans))
for i in ans:
    print(i)