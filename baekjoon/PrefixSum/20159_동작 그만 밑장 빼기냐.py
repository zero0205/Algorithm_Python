n = int(input())
x = list(map(int, input().split()))

odd = [0] * (n//2+1)
even = [0] * (n//2+1)
for i in range(0, n, 2):
    even[i//2+1] = even[i//2] + x[i]
    odd[i//2+1] = odd[i//2] + x[i+1]

ans = 0
for i in range(n):  # i번째 카드에서 밑장을 뺀다면
    if i % 2 == 0:
        ans = max(ans, even[i//2]+(odd[-1]-odd[i//2]))
    else:
        ans = max(ans, even[i//2+1]+(odd[-2]-odd[i//2]))
print(ans if ans != 0 else even[-1])
