n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

ans = 0
for i in range(n):
    s, e = i+1, n-1
    while s <= e:
        mid = (s+e)//2
        if a[i]+a[mid] == x:
            ans += 1
            break
        elif a[i]+a[mid] < x:
            s = mid+1
        else:
            e = mid-1
print(ans)
