s = input()

flag = False
idx = 0
ans = ''
reverse_str = ''
while idx < len(s):
    # 태그 안의 문자 or 태그 끝
    if flag:
        if s[idx] == '>':
            flag = False
        ans += s[idx]
        idx += 1
        continue
    # 태그 시작
    if s[idx] == '<':
        flag = True
        idx += 1
        # 뒤집어놓은 문자열 붙여주기
        ans += reverse_str
        ans += '<'
        # 뒤집어놓은 문자열 저장하던 변수 초기화
        reverse_str = ''
        continue
    # 공백
    if s[idx] == ' ':
        # 뒤집어놓은 문자열 붙여주기
        ans += reverse_str
        ans += ' '
        # 뒤집어놓은 문자열 저장하던 변수 초기화
        reverse_str = ''
        idx += 1
        continue
    # 문자열인 경우
    reverse_str = s[idx] + reverse_str
    idx += 1
    
if len(reverse_str) != 0:
    ans += reverse_str

print(ans)