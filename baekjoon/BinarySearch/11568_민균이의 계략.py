################## 이분탐색 ##################
n = int(input())
cards = list(map(int, input().split()))
lis = [cards[0]]

# arr에서 v가 들어갈 위치 찾기
def binary_search(l, r, v, arr):
    while l < r:
        mid = (l+r) // 2
        if arr[mid] < v:
            l = mid + 1
        else:
            r = mid
    return r

for i in range(1, n):
    pos = binary_search(0, len(lis), cards[i], lis)
    if pos >= len(lis):
        lis.append(cards[i])
    else:
        lis[pos] = cards[i]
print(len(lis))