split_ip = input().split(':')

ans = []
second_rule = False
for group in split_ip:
    if len(group) == 0: 
        if not second_rule: # 2번째 규칙 아직 사용X
            second_rule = True
            for _ in range(9-len(split_ip)):
                ans.append("0000")
        else:
            ans.append("0000")
    elif 0 < len(group) <= 4:
        ans.append('0'*(4-len(group)) + group)
    elif len(group) == 4:
        ans.append(group)
print(':'.join(ans))