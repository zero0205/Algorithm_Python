import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort()  # 정렬


def bs(dot):
    s, e = 0, n-1
    while s <= e:
        mid = (s+e)//2
        if dots[mid] == dot:
            return True
        elif dots[mid] > dot:
            e = mid-1
        else:
            s = mid+1
    return False


cnt = 0
for dot in dots:
    left_top = (dot[0], dot[1]+b)
    right_bottom = (dot[0]+a, dot[1])
    right_top = (dot[0]+a, dot[1]+b)
    if bs(left_top) and bs(right_bottom) and bs(right_top):
        cnt += 1
print(cnt)
