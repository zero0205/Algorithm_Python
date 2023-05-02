n, k = map(int, input().split())

start, end = 0, n//2+1
while start <= end:
    mid = (start+end) // 2
    piece = (n+1-mid) * (mid+1) # 조각 개수
    if piece == k:
        print("YES")
        exit()
    if piece > k:
        end = mid - 1
    else:
        start = mid + 1
        
print("NO")