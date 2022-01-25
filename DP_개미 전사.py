# n : 식량 창고의 개수 
n = int(input())
arr = list(map(int, input().split()))

# 다이나믹 프로그래밍을 위한 배열 선언
d = [0] * n

d[0] = arr[0]
d[1] = arr[1]

for i in range(2, len(arr)):
    d[i] = max(d[:i-1]) + arr[i]
    
print(max(d))


#######수정 코드#######
# n : 식량 창고의 개수 
n = int(input())
arr = list(map(int, input().split()))

# 다이나믹 프로그래밍을 위한 배열 선언
d = [0] * n

d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + arr[i])
    
print(d[n-1])