# 가능한 연산 : 5, 3, 2로 나누기(나누어 떨어진다면) / 1 빼기

array = [0] * 30001

def func(x, arr, cnt):
    if x == 1:
        return
    if x % 5 == 0:
        if arr[x//5] > cnt + 1 or arr[x//5] == 0:
            arr[x//5] = cnt + 1
            func(x//5, arr, cnt + 1)
    if x % 3 == 0:
        if arr[x//3] > cnt + 1 or arr[x//3] == 0:
            arr[x//3] = cnt + 1
            func(x//3, arr, cnt + 1)
    if x % 2 == 0:
        if arr[x//2] > cnt + 1 or arr[x//2] == 0:
            arr[x//2] = cnt + 1
            func(x//2, arr, cnt + 1)
    if arr[x-1] > cnt + 1 or arr[x-1] == 0:
        arr[x-1] = cnt + 1
        func(x-1, arr, cnt + 1)

# x 입력받기
x = int(input())

func(x, array, 0)
print(array[1])