# n 입력받기
n = int(input())
# 수열 입력받기
arr = list(map(int, input().split()))

start = 0
end = n - 1

while start <= end:
    mid = (start + end) // 2
    if mid == arr[mid]:
        print(mid)  # 고정점 출력
        break
    if arr[mid] < mid:
        start = mid + 1
    if arr[mid] > mid:
        end = mid - 1
        
if start > end:
    print(-1)