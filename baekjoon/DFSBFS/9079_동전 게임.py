from collections import deque

def flip(coin, m, n = 0):   # 뒤집을 배열, 뒤집는 방법, n번째 줄(대각선일때는 사용X)
    # n번째 행 뒤집기
    if m == 0:
       coin ^= int(0b111000000 >> 3 * n)
    # n번째 열 뒤집기        
    elif m == 1:
        coin ^= int(0b100100100 >> n)
    # 왼위->오른아래 대각선 뒤집기  
    elif m == 2:
        coin ^= int(0b100010001)
    # 오른위->왼아래 대각선 뒤집기
    elif m == 3:
        coin ^= int(0b001010100)
    return coin

# 코인이 모두 같은 면인지 확인
def check(coin):    
    return True if (coin == 0 or coin == 511) else False
    
for _ in range(int(input())):
    coin = 0
    for _ in range(3):  
        for c in list(input().split()):
            coin = coin << 1
            if c == 'H':    # H는 1, T는 0
                coin += 1
                
    # 코인 확인
    visited = [False] * 1000
    visited[coin] = True
    q = deque([[coin, 0]])
    find = False
    while q:
        now, cnt = q.popleft()
        if check(now):
            print(cnt)
            find = True
            break
        for i in range(4):  # 뒤집는 방법
            if i < 2:   # 행 열 뒤집기
                for j in range(3):  # 뒤집을 줄
                    tmp = flip(now, i, j)
                    if not visited[tmp]:
                        q.append([tmp, cnt+1])
                        visited[tmp] = True
            else:   # 대각선 뒤집기
                tmp = flip(now, i)
                if not visited[tmp]:
                    q.append([tmp, cnt+1])
                    visited[tmp] = True
                    
    if not find:
        print(-1)