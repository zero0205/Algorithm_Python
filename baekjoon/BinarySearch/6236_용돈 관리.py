n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]


def chk(k):  # m번 이하로 인출할 수 있는지
    if k < max(money):  # n일 중 가장 많이 쓰는 날보다 작아서는 안됨
        return int(1e9)
    tmp = 0
    cnt = 0
    for i in range(n):
        if tmp < money[i]:    # 인출
            tmp = k
            cnt += 1
        tmp -= money[i]  # i번째 날 사용
    return cnt


# 매개 변수 탐색
s, e = 0, int(1e9)
while s <= e:
    k = (s+e)//2
    if chk(k) <= m:
        e = k-1
    else:
        s = k+1

print(e+1)
