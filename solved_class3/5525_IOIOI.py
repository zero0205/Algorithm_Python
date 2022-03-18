# https://www.acmicpc.net/problem/5525

n = int(input())
m = int(input())
s = input()

p = "I"
for i in range(n * 2):
    if i % 2 == 0:
        p += 'O'
    else:
        p += 'I'

res = 0
for j in range(m):
    end_idx = j + 2 * n + 1
    if end_idx >= m:
        break
    if s[j] == 'O':
        continue
    if s[j:end_idx] == p:
        res += 1
        
print(res)