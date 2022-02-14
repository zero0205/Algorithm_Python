# N 입력받기
n = int(input())
# 매장에 있는 부품들 번호
a = list(map(int, input().split()))

# M 입력받기
m = int(input())
# 손님이 요청한 부품 번호
b = list(map(int, input().split()))

# 매장에 있는 부품들 번호 정렬
a.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    if array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)

for i in b:
    if binary_search(a, i, 0, len(a)) == None:
        print("no", end = ' ')
    else:
        print("yes", end=' ')