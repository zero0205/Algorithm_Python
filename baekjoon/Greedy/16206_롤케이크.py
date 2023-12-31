n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(key=lambda x: (x % 10, x))  # 10으로 나눴을 때의 나머지로 오름차순
print(*arr)

ans = 0
for a in arr:
    # 롤케이크 길이가 10의 배수
    if a % 10 == 0:
        cutting = a//10 - 1
        if cutting > m:
            ans += m
        else:
            ans += (cutting+1)
    # 롤케이크 길이가 10의 배수 아님
    else:
        cutting = a//10
        if cutting > m:
            ans += m
        else:
            ans += cutting
    m -= cutting
    if m <= 0:
        break
print(ans)
