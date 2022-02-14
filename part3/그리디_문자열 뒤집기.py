# 문자열 S 입력받기
s = input()

prev = s[0]
if prev == '0':
    cnt_0 = 1
    cnt_1 = 0
else:
    cnt_0 = 0
    cnt_1 = 1
# 문자열에서 연속된 0의 그룹 개수, 연속된 1의 그룹 개수 세기
for i in s[1:]:
    if i == prev:   # 이전 인덱스와 같다면 그룹의 수 증가 X
        continue
    else:
        if i == '0':
            cnt_0 += 1
        else:
            cnt_1 += 1
    prev = i
    
print(min(cnt_0, cnt_1))