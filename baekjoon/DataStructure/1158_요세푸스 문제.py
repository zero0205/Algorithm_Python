n, k = map(int, input().split())

print("<", end="")

arr = [i for i in range(1, n+1)]
idx = 0

while arr:
    idx += (k-1)
    if len(arr) == 1:
        print(arr[0], end='')
        break
    idx %= len(arr)
    print(arr[idx], ", ", sep='', end='')
    del arr[idx]
    
print(">")