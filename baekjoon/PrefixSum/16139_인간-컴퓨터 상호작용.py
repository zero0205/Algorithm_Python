import sys
input = sys.stdin.readline

s = input().rstrip()
acc = [[0] * 26 for _ in range(len(s)+1)]
for i in range(1, len(s)+1):
    for j in range(26):
            acc[i][j] = acc[i-1][j]
    acc[i][ord(s[i-1])-97] += 1

q = int(input())
for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    print(acc[r+1][ord(a)-97]-acc[l][ord(a)-97])