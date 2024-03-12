n = int(input())
room = [input() for _ in range(n)]

# 가로(행)
row = 0
for i in range(n):
    tmp = 0
    for j in range(n):
        if room[i][j] == 'X':
            if tmp >= 2:
                row += 1
            tmp = 0
        else:
            tmp += 1
    if tmp >= 2:
        row += 1
# 세로(열)
col = 0
for j in range(n):
    tmp = 0
    for i in range(n):
        if room[i][j] == 'X':
            if tmp >= 2:
                col += 1
            tmp = 0
        else:
            tmp += 1
    if tmp >= 2:
        col += 1
print(row, col)
