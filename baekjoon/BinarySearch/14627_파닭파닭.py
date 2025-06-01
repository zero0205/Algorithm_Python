import sys
input = sys.stdin.readline

s, c = map(int, input().split())
green_onion = [int(input()) for _ in range(s)]

answer = 0
l, r = 1, max(green_onion)
while l <= r:
    mid = (l+r)//2

    chicken = 0
    ramyeon = 0
    for go in green_onion:
        chicken += go // mid
        ramyeon += go % mid

    if chicken >= c:
        l = mid+1
        answer = ramyeon + (chicken-c)*mid
    else:
        r = mid-1

print(answer)
