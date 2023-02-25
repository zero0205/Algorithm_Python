import sys
input = sys.stdin.readline

def rotate(n, m, arr):
    for i in range(min(n, m) // 2):
        row = n - i*2   # 세로 길이
        col = m - i*2   # 가로 길이
        
        top = []        
        bottom = []
        for j in range(i, i+col):
            top.append(arr[i][j])
            bottom.append(arr[n-1-i][j])
        left = []
        right = []
        for j in range(i, i+row):
            left.append(arr[j][i])
            right.append(arr[j][m-1-i])
        
        # 시작은 i, 끝은 n-1-i / m-1-i
        # 윗줄
        for j in range(1, col):
            arr[i][i+j-1] = top[j]
        # 아랫줄
        for j in range(1, col):
            arr[n-1-i][i+j] = bottom[j-1]
        # 왼쪽
        for j in range(1, row):
            arr[i+j][i] = left[j-1]
        # 오른쪽
        for j in range(1, row):
            arr[i+j-1][m-1-i] = right[j]
            
    
n, m, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# r번 회전
for _ in range(r):
    rotate(n, m, arr)
for i in range(n):
    print(*arr[i])