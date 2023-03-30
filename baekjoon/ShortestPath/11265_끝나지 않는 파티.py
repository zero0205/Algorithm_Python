import sys
input = sys.stdin.readline

n, m  = map(int, input().split())
travel_time = [[] for _ in range(n+1)]
for i in range(1, n+1):
    travel_time[i] = [0] + list(map(int, input().split()))
    
# 플로이드-워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if travel_time[i][j] >  travel_time[i][k]+travel_time[k][j]:
                travel_time[i][j] = travel_time[i][k]+travel_time[k][j]
            
for _ in range(m):
    a, b, c = map(int, input().split())
    if travel_time[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")