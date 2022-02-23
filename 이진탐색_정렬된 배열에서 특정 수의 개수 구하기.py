# n, x 입력받기
n, x = map(int, input().split())
# 수열 입력받기
arr = list(map(int, input().split()))

start = 0
end = n - 1

# 이진 탐색
while start <= end:
    mid = (start + end) // 2
    # x 찾음
    if arr[mid] == x:
        break
    if arr[mid] < x : 
        start = mid + 1
    elif arr[mid] > x:
        end = mid - 1
        
# 값이 x인 원소가 없는 경우
if start > end:
    print(-1)
else:
    right = mid + 1
    left = mid - 1
    cnt = 1
    while arr[right] == x or arr[left] == x:
        if arr[right] == x:
            right += 1
            cnt += 1
        if arr[left] == x:
            left -= 1
            cnt += 1
    print(cnt)