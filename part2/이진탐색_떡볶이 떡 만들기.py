# n : 떡의 개수, m : 손님이 요청한 떡의 길이
from functools import total_ordering
import re
from unittest import result


n, m = map(int, input().split())
ddeok = list(map(int, input().split()))

start = min(ddeok)
end = max(ddeok)

cnt = len(ddeok)
res = 0

while start <= end:
    sum = 0
    mid = (start + end) // 2
    
    for i in ddeok:
        if i < mid:
            continue
        sum += (i - mid)
        
    # 원하는 양보다 적게 잘라짐 -> 높이 내려야지
    if sum < m:
        end = mid - 1
    # 원하는 양보다 많이 잘라짐 -> 높이 올려야지
    else:
        res = mid
        start = mid + 1
        