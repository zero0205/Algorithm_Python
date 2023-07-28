n, q = map(int, input().split())
cows = list(map(int, input().split()))
joke = list(map(int, input().split()))

arr = [1] * n
total = 0   # S
for i in range(n):
    for j in range(4):
        arr[i] *= cows[(i+j)%n]
    total += arr[i]

for i in range(q):
    for j in range(4):
        arr[(joke[i]-1-j)%n] *= (-1)
        total += arr[(joke[i]-1-j)%n] * 2
    print(total)