# 케이크 자르기
# k개의 좌표가 주어지면 가로, 세로에 평행하게 자름
# 가로 m, 세로 n
# 0 < x_i < m
# 0 < y_i < n

n, m, k = map(int, input().split())
x_pos = [0]
y_pos = [0]
for _ in range(k):
    x, y = map(int, input().split())
    x_pos.append(x)
    y_pos.append(y)
x_pos.sort()
y_pos.sort()
x_pos.append(m)
y_pos.append(n)

min_w = int(1e9)
max_w = 0
min_h = int(1e9)
max_h = 0
for i in range(1, k+2):
    w = x_pos[i] - x_pos[i-1]
    h = y_pos[i] - y_pos[i-1]
    # 가로
    if min_w > w:
        min_w = w
    if max_w < w:
        max_w = w
    # 세로
    if min_h > h:
        min_h = h
    if max_h < h:
        max_h = h
        
print(min_w*min_h, max_w*max_h)
# 6 7 2
# 2 1
# 6 4
# 정답 : 1 12