# 구현
# 예제 2. 시각

n = int(input())

h, m, s = 0, 0, 0
res = 0

# 시간
for i in range(n+1):
    if str(i).find('3') != -1:
        res += 60 * 60
        continue
    # 분
    for j in range(60):
        if str(j).find('3') != -1:
            res += 60
            continue
        # 초
        for k in range(60):
            if str(k).find('3') != -1:
                res += 1

print(res)