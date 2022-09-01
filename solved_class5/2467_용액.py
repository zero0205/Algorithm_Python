n = int(input())

liquid = [i for i in list(map(int, input().split()))]

start, end = 0, n-1
l, r = 0, 0
minimum = int(1e9) * 2

while start < end:
    sum = liquid[start] + liquid[end]
    if minimum > abs(sum):
        l = start
        r = end
        minimum = abs(sum)
    if sum < 0:
        start += 1
    else:
        end -= 1

print(liquid[l], liquid[r])