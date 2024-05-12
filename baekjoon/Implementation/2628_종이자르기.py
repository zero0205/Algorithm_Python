n, m = map(int, input().split())
row, col = [0, m], [0, n]
for _ in range(int(input())):
    num, line = map(int, input().split())
    if num == 0:    # 가로
        row.append(line)
    else:           # 세로
        col.append(line)


def longest(arr):   # arr에 저장된 선분 간의 길이 중 가장 긴 것 리턴
    arr.sort()
    res = 0
    for i in range(1, len(arr)):
        if arr[i]-arr[i-1] > res:
            res = arr[i]-arr[i-1]
    return res


print(longest(row)*longest(col))
