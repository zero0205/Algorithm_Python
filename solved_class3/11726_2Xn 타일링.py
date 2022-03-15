# https://www.acmicpc.net/problem/11726

# n 입력받기
n = int(input())

tile = [0, 1, 2]

for i in range(3, n + 1):
    tile.append(tile[i-1] + tile[i-2])
    
print(tile[n] % 10007)