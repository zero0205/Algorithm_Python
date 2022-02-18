# https://www.acmicpc.net/problem/18405
import sys
import heapq

# n : 시험관의 가로세로 크기, k : 바이러스 1~k번까지 존재
n, k = map(int, input().split())
# 시험관 정보 입력
testTube = []
for _ in range(n):
    testTube.append(list(map(int, sys.stdin.readline().split())))
# s : 경과 시간, x, y : 좌표
s, x, y = map(int, input().split())

def virus_spread(graph, heap, n):
    dir = [(-1,0),(1,0),(0,-1),(0,1)]   # 상하좌우
    new_h = []
    while heap:
        v, r,c = heapq.heappop(heap)
        for d in dir:
            nr = r + d[0]
            nc = c + d[1]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if graph[nr][nc] == 0:
                heapq.heappush(new_h, (v, nr, nc))
                graph[nr][nc] = v
    return new_h

# 처음 바이러스 있는 위치들 저장하는 최소힙(바이러스 번호, x좌표, y 좌표)
virus = []
for r in range(n):
    for c in range(n):
        if testTube[r][c] != 0:
            heapq.heappush(virus, (testTube[r][c], r, c))



for sec in range(s):
    # (sec + 1)초 경과 시 바이러스 퍼지는 현황
    virus = virus_spread(testTube, virus, n)

print(testTube[x-1][y-1])