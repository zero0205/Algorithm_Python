# https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    sticker = []
    sticker.append(list(map(int, input().split())))
    sticker.append(list(map(int, input().split())))

    for i in range(1, n):
        if i == 1:
            sticker[0][i] += sticker[1][i-1]
            sticker[1][i] += sticker[0][i-1]
        else:
            sticker[0][i] += max(sticker[1][i-2], sticker[1][i-1])
            sticker[1][i] += max(sticker[0][i-2], sticker[0][i-1])
        
    print(max(sticker[0][n-1], sticker[1][n-1]))