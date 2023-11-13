n, m = map(int, input().split())
matrix_a = []
matrix_b = []
for i in range(n):
    matrix_a.append(list(input()))
for i in range(n):
    matrix_b.append(list(input()))
cnt = 0
if n >= 3 and m >= 3:
    for i in range(n-2):
        for j in range(m-2):
            if matrix_a[i][j] != matrix_b[i][j]:
                # 3X3 뒤집기
                for p in range(3):
                    for q in range(3):
                        if matrix_a[i+p][j+q] == '0':
                            matrix_a[i+p][j+q] = '1'
                        else:
                            matrix_a[i+p][j+q] = '0'
                cnt += 1
for i in range(n):
    for j in range(m):
        if matrix_a[i][j] != matrix_b[i][j]:
            cnt = -1
print(cnt)
