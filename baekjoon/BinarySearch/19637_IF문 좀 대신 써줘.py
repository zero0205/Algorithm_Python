import sys
input = sys.stdin.readline

n, m = map(int, input().split())
title = []
# 전투력 상한값의 비내림차순으로 주어짐
for _ in range(n):
    title.append(input().split())

def find_title(character):
    max_idx = 0
    start, end = 0, len(title)-1
    while start <= end:
        mid = (start + end) // 2
        if int(title[mid][1]) < character:
            start = mid + 1
        else:
            max_idx = mid
            end = mid - 1
    return title[max_idx][0]

for _ in range(m):
    print(find_title(int(input())))