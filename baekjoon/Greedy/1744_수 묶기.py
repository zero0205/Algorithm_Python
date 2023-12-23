def get_max_sum(arr):
    res = 0
    prev = 1001
    for i in range(len(arr)):
        if prev == 1001:
            prev = arr[i]
        else:
            res += prev * arr[i]
            prev = 1001
    res += (0 if prev == 1001 else prev)
    return res


n = int(input())
pos = []
neg = []
ans = 0
for _ in range(n):
    tmp = int(input())
    if tmp > 1:
        pos.append(tmp)
    elif tmp == 1:
        ans += 1
    else:
        neg.append(tmp)

pos.sort(reverse=True)  # 내림차순 정렬
neg.sort()  # 오름차순 정렬

ans += (get_max_sum(pos)+get_max_sum(neg))
print(ans)
