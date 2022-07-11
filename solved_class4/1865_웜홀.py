import sys
input = sys.stdin.readline

INF = int(1e9)

tc = int(input())   # 테스트케이스의 개수
for i in range(tc):
    n, m, w = map(int, input().split())
    
    road = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    # 자기 자신으로 가는 건 0으로 초기화
    for i in range(n + 1):
        road[i][i] = 0
    
    # 도로의 정보 입력
    for _ in range(m): 
        s, e, t = map(int, input().split())
        road[s][e] = t
        road[e][s] = t
    # 웜홀의 정보 입력
    for _ in range(w):
        s, e, t = map(int, input().split())
        road[s][e] = -t

    flag = False                

    # 플로이드 와샬
    for k in range(1, n + 1):
        if flag:
            break
        for i in range(1, n + 1):
            if flag:
                break
            for j in range(1, n + 1):
                road[i][j] = min(road[i][j], road[i][k] + road[k][j])
                if i == j and road[i][j] < 0:
                    flag = True
                    break
    for j in range(1, n + 1):
        if road[j][j] < 0:
            flag = True
            break
    if flag:
        print("YES")
    else:
        print("NO")