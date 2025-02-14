n, k = map(int, input().split())
orders = list(map(int, input().split()))

answer = 0
multitap = set()
for i in range(k):
    # 이미 꽂혀있는지 확인
    if orders[i] in multitap:
        continue
    # 빈 칸이 있는지 확인
    if len(multitap) < n:
        multitap.add(orders[i])
        continue
    # 교체
    change_plug = -1
    max_latest_use = -1
    for plug in multitap:
        if plug not in orders[i+1:]:
            change_plug = plug
            break
        latest_use = orders[i+1:].index(plug)
        if latest_use > max_latest_use:
            change_plug = plug
            max_latest_use = latest_use
    multitap.remove(change_plug)
    multitap.add(orders[i])
    answer += 1
print(answer)
