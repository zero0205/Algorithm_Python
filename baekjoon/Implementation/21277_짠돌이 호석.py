n1, m1 = map(int, input().split())
board1 = [list(input()) for _ in range(n1)]
n2, m2 = map(int, input().split())
board2 = [list(input()) for _ in range(n2)]


def rotate(b):  # 시계방향 90도 회전
    global n2, m2
    new_b = [[None]*len(b) for _ in range(len(b[0]))]
    for i in range(len(b)):
        for j in range(len(b[0])):
            new_b[j][len(b)-1-i] = b[i][j]
    n2, m2 = len(new_b), len(new_b[0])
    return new_b


# bb에 board1은 고정시켜놓고, board2를 90도씩 돌려서 옮기며 비교
bb = [[0]*151 for _ in range(151)]

# bb에 (50, 50)부터 board1 고정
for i in range(50, 50+n1):
    for j in range(50, 50+m1):
        bb[i][j] = board1[i-50][j-50]

ans = 10000
for d in range(4):  # 방향
    for i in range(50-n2, 50+n1+1):  # board2의 시작 행
        for j in range(50-m2, 50+m1+1):  # board2의 시작 열
            # i, j를 시작점으로 하는 board2가 board1과 겹치는지?
            possible = True
            for r in range(i, i+n2):
                for c in range(j, j+m2):
                    if bb[r][c] == '1' and board2[r-i][c-j] == '1':
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                x1 = min(i, 50)
                y1 = min(j, 50)
                x2 = max(i+n2-1, 49+n1)
                y2 = max(j+m2-1, 49+m1)
                area = (x2-x1+1)*(y2-y1+1)
                if area < ans:
                    ans = area
    board2 = rotate(board2)


print(ans)
