import sys
input = sys.stdin.readline

n = int(input())
sheet = [0] + list(map(int, input().split()))
mistake = [0] * (n+1)
for i in range(1, n):
    mistake[i] = mistake[i-1] + (1 if sheet[i] > sheet[i+1] else 0)
mistake[n] = mistake[n-1]

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(mistake[y-1]-mistake[x-1])