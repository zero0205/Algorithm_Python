def rotating(arr, cmd):
    n = len(arr)
    m = len(arr[0])
    # command 1 => 상하 반전
    if cmd == 1:
        new_arr = []
        for i in range(n-1, -1, -1):
            new_arr.append(arr[i])
    # command 2 => 좌우 반전
    elif cmd == 2:
        new_arr = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                new_arr[i][j] = arr[i][m-1-j]
    # command 3 => 오른쪽으로 90도 회전
    elif cmd == 3:
        new_arr = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_arr[i][j] = arr[n-1-j][i]
    # command 4 => 왼쪽으로 90도 회전
    elif cmd == 4:
        new_arr = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_arr[i][j] = arr[j][m-1-i]
    else:
        new_arr = [[0]*m for _ in range(n)]
        # command 5 => 4개의 부분 배열로 나눠서 시계 방향 회전
        if cmd == 5:
            for i in range(n//2):
                for j in range(m//2):
                    new_arr[i][j] = arr[i+n//2][j]
                    new_arr[i][j+m//2] = arr[i][j]
                    new_arr[i+n//2][j+m//2] = arr[i][j+m//2]
                    new_arr[i+n//2][j] = arr[i+n//2][j+m//2]
        # command 6 => 4개의 부분 배열로 나눠서 반시계 방향 회전
        else:
            for i in range(n//2):
                for j in range(m//2):
                    new_arr[i][j] = arr[i][j+m//2]
                    new_arr[i][j+m//2] = arr[i+n//2][j+m//2]
                    new_arr[i+n//2][j+m//2] = arr[i+n//2][j]
                    new_arr[i+n//2][j] = arr[i][j]
    return new_arr


n, m, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for cmd in list(map(int, input().split())):
    arr = rotating(arr, cmd)

for i in range(len(arr)):
    print(*arr[i])
