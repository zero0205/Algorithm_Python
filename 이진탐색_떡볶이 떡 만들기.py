# n : 떡의 개수, m : 손님이 요청한 떡의 길이
n, m = map(int, input().split())
ddeok = list(map(int, input().split()))

mid = min(ddeok)
cnt = len(ddeok)

while True:
    sum_d = sum(ddeok) - cnt * mid
    
    if m == sum_d