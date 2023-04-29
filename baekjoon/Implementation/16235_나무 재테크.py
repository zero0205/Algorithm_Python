import sys
from collections import deque
input = sys.stdin.readline

# 봄 => 양분 먹고 나이 증가
def spring():
    for r in range(n):
        for c in range(n):
            for i in range(len(trees[r][c])):
                if map_data[r][c] >= trees[r][c][i]:
                    map_data[r][c] -= trees[r][c][i]    # 나무가 양분 먹음
                    trees[r][c][i] += 1 # 나무 나이 증가
                else:
                    # 여름 => 죽은 나무는 양분이 됨
                    for j in range(i, len(trees[r][c])):
                        map_data[r][c] += trees[r][c].pop()//2
                    break

# 가을 => 나무 번식
def autumn():
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    for r in range(n):
        for c in range(n):
            for tree in trees[r][c]:
                if tree % 5 == 0:
                    for i in range(8):
                        nx = r + dx[i]
                        ny = c + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            trees[nx][ny].appendleft(1)

# 겨울 => s2d2가 땅에 양분 추가
def winter():
    for i in range(n):
        for j in range(n):
            map_data[i][j] += s2d2[i][j]

n, m, k = map(int, input().split())
map_data = [[5]*n for _ in range(n)]    # 땅 양분 정보
# 각 칸에 추가되는 양분
s2d2 = []
for _ in range(n):
    s2d2.append(list(map(int, input().split())))
    
# 나무 정보
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    # 나무 위치(x, y), 나무 나이 z
    trees[x-1][y-1].append(z)
    
for i in range(k):
    spring()
    autumn()
    winter()        
    
ans = 0
for r in range(n):
    for c in range(n):
        ans += len(trees[r][c])
print(ans)  