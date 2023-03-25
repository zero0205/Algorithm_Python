import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
dic = defaultdict(int)
for _ in range(n):
    name, extension  = input().strip().split('.')
    dic[extension] += 1

for ex, num in sorted(dic.items()):
    print(ex, num)