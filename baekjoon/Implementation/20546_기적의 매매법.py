jh_money = sm_money = int(input())
machineduck = list(map(int, input().split()))

jh_stock = sm_stock = 0

cnt = 0
for i in range(14):
    # 준현 (BNP)
    jh_stock += jh_money // machineduck[i]
    jh_money = jh_money % machineduck[i]
    # 성민 (TIMING)
    if i == 0:
        continue
    if machineduck[i-1] < machineduck[i]:   # 전일 대비 가격 상승
        if cnt >= 1:
            cnt += 1
        else:
            cnt = 1
        if cnt >= 3:    # 3일 연속 상승 -> 전량 매도
            sm_money += sm_stock * machineduck[i]
            sm_stock = 0
    elif machineduck[i-1] > machineduck[i]: # 전일 대비 가격 하락
        if cnt <= -1:
            cnt -= 1
        else:
            cnt = -1
        if cnt <= -3:   # 3일 연속 하락 -> 전량 매수
            sm_stock += sm_money // machineduck[i]
            sm_money = sm_money % machineduck[i]

# 1월 14일의 자산 계산 
jh = jh_money + jh_stock * machineduck[-1] 
sm = sm_money + sm_stock * machineduck[-1] 

if jh > sm:
    print("BNP")
elif sm == jh:
    print("SAMESAME")
else:
    print("TIMING")