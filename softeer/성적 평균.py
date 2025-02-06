import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))

# 누적합
acc = [0]
for i in range(n):
    acc.append(acc[-1]+s[i])

for _ in range(k):
    a, b = map(int, input().split())
    avg = (acc[b]-acc[a-1])/(b-a+1)
    print(f"{round(avg, 2):.2f}")
