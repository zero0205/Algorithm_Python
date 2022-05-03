# https://www.acmicpc.net/problem/10830

n, b = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i].extend(list(map(int, input().split())))

# 행렬의 곱하기 = (1번째 행렬의 n행 * 2번째 행렬의 n열)의 합
def matrix_mult(arr1, arr2):
    ans = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for k in range(n):
                ans[r][c] += (arr1[r][k] * arr2[k][c])
            ans[r][c] %= 1000
    return ans

def matrix_pow(arr, num):
    if num == 1:
        for r in range(n):
            for c in range(n):
                arr[r][c] %= 1000
        return arr
    tmp = matrix_pow(arr, num // 2) 
    if num % 2 == 0:
        return matrix_mult(tmp, tmp)
    else:
        return matrix_mult(arr, matrix_mult(tmp, tmp))
    
ans = matrix_pow(arr, b)
for r in range(n):
    for c in range(n):
        print(ans[r][c], end=" ")
    print()