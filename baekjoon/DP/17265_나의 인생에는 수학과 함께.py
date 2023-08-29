n = int(input())
map_data = []
for _ in range(n):
    map_data.append(list(input().split()))

v = [[[int(1e9), -int(1e9)] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            v[0][0][0] = int(map_data[0][0])
            v[0][0][1] = int(map_data[0][0])
            continue
        # 연산자
        if (i+j) % 2 == 1:
            if i == 0:
                v[i][j][0] = v[i][j-1][0]
                v[i][j][1] = v[i][j-1][1]
                continue
            if j == 0:
                v[i][j][0] = v[i-1][j][0]
                v[i][j][1] = v[i-1][j][1]
                continue
            v[i][j][0] = min(v[i-1][j][0], v[i][j-1][0])
            v[i][j][1] = max(v[i-1][j][1], v[i][j-1][1])
        # 숫자
        else:
            if i == 0:
                v[i][j][0] = eval(
                    str(v[i][j-1][0])+map_data[i][j-1]+map_data[i][j])
                v[i][j][1] = eval(
                    str(v[i][j-1][1])+map_data[i][j-1]+map_data[i][j])
                continue
            if j == 0:
                v[i][j][0] = eval(
                    str(v[i-1][j][0])+map_data[i-1][j]+map_data[i][j])
                v[i][j][1] = eval(
                    str(v[i-1][j][1])+map_data[i-1][j]+map_data[i][j])
                continue
            v[i][j][0] = min(eval(str(v[i-1][j][0])+map_data[i-1][j]+map_data[i][j]),
                             eval(str(v[i][j-1][0])+map_data[i][j-1]+map_data[i][j]))
            v[i][j][1] = max(eval(str(v[i-1][j][1])+map_data[i-1][j]+map_data[i][j]),
                             eval(str(v[i][j-1][1])+map_data[i][j-1]+map_data[i][j]))
print(v[n-1][n-1][1], v[n-1][n-1][0])
