x, y, w, s = map(int, input().split())

# 평행 이동만
case1 = (x+y)*w
# 최대한 대각선 이동
if (x+y) % 2 == 0:  # 대각선 이동만 해도 됨
    case2 = max(x, y)*s
else:   # 1번은 평행 이동 필요
    case2 = (max(x, y)-1)*s+w
# 평행 + 대각선
case3 = min(x, y)*s + abs(x-y)*w

print(min(case1, case2, case3))
