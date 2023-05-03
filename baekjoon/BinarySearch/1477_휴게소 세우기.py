n, m, l = map(int, input().split())
rest = [0] + sorted(list(map(int, input().split()))) + [l]

start, end = 1, l
ans = 0
while start <= end:
    cnt = 0
    mid = (start+end)//2
    
    for i in range(1, n+2):
        gap = rest[i] - rest[i-1]
        if gap > mid:   # 현재 mid 값보다 휴게소 간 거리가 멀다면 휴게소 설치
            cnt += (gap-1) // mid   # 현재 설치된 휴게소들은 제외해야 하므로 -1
            
    if cnt > m: # 설치하려는 개수보다 더 설치가 필요한 경우 거리를 늘려야 함
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
        
print(ans)