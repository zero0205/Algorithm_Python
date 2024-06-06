import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))  # k번 섞은 후의 카드
d = list(map(int, input().split()))  # 셔플 정보


def reverse_shuffle(arr):
    res = [0]*n
    for i in range(n):
        res[d[i]-1] = arr[i]
    return res


tmp = s[:]
for _ in range(k):
    tmp = reverse_shuffle(tmp)

print(*tmp)
