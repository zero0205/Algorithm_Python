import sys
input = sys.stdin.readline
<<<<<<< HEAD

n, magic, k = map(int, input().split())
fireball = []
=======
from collections import deque

n, magic, k = map(int, input().split())
fireball = deque()
>>>>>>> b5672a5f1244820745b9b9b19892bf587f90d62b
for _ in range(magic):
    # r, c, m, s, d (행 열 질량 속력 방향)
    r, c, m, s, d = map(int, input().split())
    fireball.append([r-1, c-1, m, s, d])
    
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    moved_fireball = [[[] for _ in range(n)] for _ in range(n)]
    # 1. 파이어볼 이동
    while fireball:
        fr, fc, fm, fs, fd = fireball.pop()
        nr = (fr + dx[fd] * fs) % n
        nc = (fc + dy[fd] * fs) % n
        moved_fireball[nr][nc].append([fm, fs, fd])            
    # 2. 파이어볼 4단 분리
    for i in range(n):
        for j in range(n):
            if len(moved_fireball[i][j]) == 0:
                continue
            elif len(moved_fireball[i][j]) == 1:
                fireball.append([i, j, moved_fireball[i][j][0][0], moved_fireball[i][j][0][1], moved_fireball[i][j][0][2]])
            else:
                tm, ts, even, num = 0, 0, 0, len(moved_fireball[i][j])
                while moved_fireball[i][j]:
                    nm, ns, nd = moved_fireball[i][j].pop()
                    tm += nm
                    ts += ns
                    if nd % 2 == 0:
                        even += 1
                if even == num or even == 0:
                    dir = 0
                else:
                    dir = 1
                if tm // 5 > 0:
                    for d in range(0, 8, 2):
                        fireball.append([i, j, tm//5, ts//num, d+dir])

for _ in range(k):
    move()
    
ans = 0
while fireball:
    ans += fireball.pop()[2]
    
print(ans)