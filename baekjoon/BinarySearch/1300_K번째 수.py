n = int(input())
k = int(input())

# A 배열에서 num보다 작은 수의 개수 구하기
def calc(num):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(n, num // i)
    return cnt

start, end = 1, k
ans = 0
while start <= end:
    mid = (start+end)//2
    if calc(mid) < k:
        start = mid + 1 
    else:
        end = mid - 1
        ans = mid
print(ans)