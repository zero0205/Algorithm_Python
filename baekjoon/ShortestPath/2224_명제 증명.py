import sys
input = sys.stdin.readline

n = int(input())
num = 0
graph = [[False] * 58 for _ in range(58)]   # 아스키 코드 (A:65 ~ z:122)
for _ in range(n):
    p, _, q = input().split()
    if p == q:
        continue
    # 아스키코드 변환
    p = ord(p) - 65
    q = ord(q) - 65
    if not graph[p][q]:
        graph[p][q] = True
        num += 1

for k in range(58):
    for i in range(58):
        for j in range(58):
            if i != j and not graph[i][j] and graph[i][k] and graph[k][j]:
                num += 1
                graph[i][j] = True

print(num)                
for i in range(58):
    for j in range(58):
        if i == j:
            continue
        if graph[i][j]:
            print(chr(i+65),"=>", chr(j+65))