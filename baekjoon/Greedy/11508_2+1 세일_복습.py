import sys
input = sys.stdin.readline

n = int(input())
diary = []
for _ in range(n):
    diary.append(int(input()))
    
diary.sort(reverse=True)

total = sum(diary)
for i in range(2, n, 3):
    total -= diary[i]

print(total)