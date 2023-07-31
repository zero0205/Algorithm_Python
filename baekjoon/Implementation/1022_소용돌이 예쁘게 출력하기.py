r1,c1,r2,c2 = map(int, input().split())
r, c = r2-r1+1, c2-c1+1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

num = 2
cnt = 0
paper = [[0] * c for _ in range(r)]
if 0 <= -r1 < r and 0 <= -c1 < c:
    paper[-r1][-c1] = 1
    cnt += 1
x, y = 1, 1
length = 2
max_num = 0
while cnt < (r*c):
    for dir in range(4):
        for _ in range(length):
            x += dx[dir]
            y += dy[dir]
            # 출력할 범위 내의 숫자인 경우
            if 0 <= x-r1 < r and 0 <= y-c1 < c:
                cnt += 1
                paper[x-r1][y-c1] = num
                max_num = num
            num += 1
    length += 2 # 한 바퀴 돌고 나면 길이 2 추가
    x += 1
    y += 1

for i in range(r):
    for j in range(c):        
        print(str(paper[i][j]).rjust(len(str(max_num))), end=' ')
    print()