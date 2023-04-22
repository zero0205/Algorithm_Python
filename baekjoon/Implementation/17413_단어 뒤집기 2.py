input_str = input()

tag = False
ans = ''
tmp = ''
for i in range(len(input_str)):
    if tag: # 태그 속의 단어
        if input_str[i] == '>': # 태그 끝남
            tag = False
        ans += input_str[i]
        continue
    # 태그 시작
    if input_str[i] == '<':
        ans += tmp
        tmp = ''
        tag = True
        ans += input_str[i]
    # 공백
    elif input_str[i] == ' ':
        ans += (tmp + ' ')
        tmp = ''
    # 단어
    else:
        tmp = input_str[i] + tmp
        
if tmp != '':
    ans += tmp
    
print(ans)