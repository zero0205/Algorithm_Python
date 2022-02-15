# https://www.acmicpc.net/problem/18406

# n 입력받기
n = input()

pre = 0
suf = 0

# 앞/뒤 반쪽 합
for i in range(len(n)//2):
    pre += int(n[i])
    suf += int(n[len(n)//2 + i])
    
if pre == suf:
    print("LUCKY")
else:
    print("READY")    