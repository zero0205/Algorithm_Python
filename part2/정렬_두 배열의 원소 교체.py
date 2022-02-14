# n, k 입력받기
n, k = map(int, input().split())

# 배열 A, B의 원소 입력받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a를 오름차순 정렬, b를 내림차순 정렬
a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))