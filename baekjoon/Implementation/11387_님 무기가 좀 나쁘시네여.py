def combat_power(info):
    attack, power, critical, critical_damage, speed = info
    result = attack
    result *= (100 + power)
    result *= (100*(100 - min(100, critical)) +
               min(100, critical)*critical_damage)
    result *= (100 + speed)
    return result


infos = [list(map(int, input().split())) for _ in range(4)]

now_cri = combat_power(infos[0])
now_paboo = combat_power(infos[1])

# 크리가 파부 무기를 장착했을 때
new_info = []
for i in range(5):
    new_info.append(infos[0][i]-infos[2][i]+infos[3][i])
new_cp = combat_power(new_info)
if new_cp > now_cri:
    print("+")
elif new_cp == now_cri:
    print("0")
else:
    print("-")
# 파부가 크리 무기를 장착했을 때
new_info = []
for i in range(5):
    new_info.append(infos[1][i]-infos[3][i]+infos[2][i])
new_cp = combat_power(new_info)
if new_cp > now_paboo:
    print("+")
elif new_cp == now_paboo:
    print("0")
else:
    print("-")
