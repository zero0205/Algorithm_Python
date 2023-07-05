# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)

# n, c = map(int, input().split())
# weight = list(map(int, input().split()))

# def dfs(idx, cnt, total):
#     if total == c:
#         print(1)
#         exit()
#     if idx >= n or cnt >= 3 or total >= c:
#         return
#     # idx번째 물건 포함 O
#     dfs(idx+1, cnt+1, total+weight[idx])
#     # idx번째 물건 포함 X
#     dfs(idx+1, cnt, total)

# dfs(0, 0, 0)
# print(0)
#####################################################
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
weight = sorted(list(map(int, input().split())))

def binary_search(start, end, target):
    while start <= end:
        mid = (start+end) // 2
        if weight[mid] == target:
            return True
        elif weight[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False
    
# 1개
if binary_search(0, n-1, c):
    print(1)
    exit()

# 2개, 3개
left, right = 0, n-1
while left < right:
    two_sum = weight[left] + weight[right]
    if two_sum == c:   # 2개로 c 만들기
        print(1)
        exit()
    elif two_sum > c:
        right -= 1
    else: 
        if binary_search(left+1, right-1, c - two_sum):   # 3개로 c 만들기
            print(1)
            exit()
        left += 1
print(0)