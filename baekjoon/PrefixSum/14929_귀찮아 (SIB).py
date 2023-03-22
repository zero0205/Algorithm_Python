n = int(input())
arr = list(map(int, input().split()))
res = 0
accumulate = [arr[0]]
for i in range(1, n):
    accumulate.append(accumulate[i-1] + arr[i])
for j in range(n):
    res += arr[j] * (accumulate[n-1] - accumulate[j])
print(res)