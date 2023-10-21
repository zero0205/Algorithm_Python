import sys
input = sys.stdin.readline

r, s = map(int, input().split())
picture = []
max_meteor = [-3000] * s
min_ground = [r-1] * s
for i in range(r):
    picture.append(input())
    for j in range(s):
        if picture[i][j] == 'X':
            max_meteor[j] = max(max_meteor[j], i)
        elif picture[i][j] == '#':
            min_ground[j] = min(min_ground[j], i)
min_air = 3000
for j in range(s):
    if min_air > (min_ground[j]-max_meteor[j]-1):
        min_air = (min_ground[j]-max_meteor[j]-1)

res = [['.']*s for _ in range(r)]

# 유성 떨어져
for i in range(r):
    for j in range(s):
        if picture[i][j] == 'X':
            res[i+min_air][j] = 'X'
        elif picture[i][j] == '#':
            res[i][j] = '#'

# 사진 출력
for i in range(r):
    for j in range(s):
        print(res[i][j], end='')
    print()
