import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    sticker = []
    sticker.append(list(map(int, input().split())))
    sticker.append(list(map(int, input().split())))
    
    if n > 1:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]
        for col in range(2, n):
            sticker[0][col] += max(sticker[1][col-1], sticker[1][col-2])
            sticker[1][col] += max(sticker[0][col-1], sticker[0][col-2])       
    print(max(sticker[0][n-1], sticker[1][n-1]))