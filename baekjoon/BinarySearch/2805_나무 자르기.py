import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = sorted(list(map(int, input().split())))

def get_sum(maximum):
    res = 0
    for t in tree:
        res += ((t-maximum) if t-maximum > 0 else 0) 
    return res

start, end = 0, tree[-1]
while start <= end:
    mid = (start + end) // 2
    if get_sum(mid) < m:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(end)