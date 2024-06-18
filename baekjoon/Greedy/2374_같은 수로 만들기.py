import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    a = int(input())
    if not arr or arr[-1] != a:
        arr.append(a)


def find_min(arr):  # 현재 배열에서 가장 작은 값과 그 인덱스 리턴
    min_v = int(1e9)+1
    min_idx = -1
    for i in range(len(arr)):
        if min_v > arr[i]:
            min_v = arr[i]
            min_idx = i
    return [min_idx, min_v]


ans = 0
while True:
    if len(arr) == 1:
        break
    min_idx, min_v = find_min(arr)
    if min_idx == 0:
        ans += arr[min_idx+1]-arr[min_idx]
    elif 0 < min_idx < len(arr)-1:
        ans += min(arr[min_idx-1], arr[min_idx+1])-arr[min_idx]
    else:
        ans += arr[min_idx-1]-arr[min_idx]
    arr.remove(min_v)

print(ans)
