# https://www.acmicpc.net/problem/1654

# 만들 수 있는 랜선의 개수 리턴
def lan_num(arr, length):
    res = 0
    for el in arr:
        res += (el // length)
    return res

k, n = map(int, input().split())
arr = []
start, end = 1, 0
for _ in range(k):
    l = int(input())
    end = max(end, l)
    arr.append(l)
    
answer = end
while start <= end:
    mid = (start + end) // 2
    if lan_num(arr, mid) >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)