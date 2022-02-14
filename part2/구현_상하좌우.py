# 구현
# 예제 1. 상하좌우

n = int(input())    # 공간의 크기 : n X n
move = input().split()

row = 1
col = 1

for mv in move:
    if mv == 'R':
        if col < n:
            col += 1
        else:
            continue
    elif mv == 'L':
        if 1 < col:
            col -= 1
        else:
            continue
    elif mv == 'U':
        if 1 < row:
            row -= 1
        else:
            continue
    elif mv == 'D':
        if row < n:
            row += 1
        else:
            continue

print(row, col)