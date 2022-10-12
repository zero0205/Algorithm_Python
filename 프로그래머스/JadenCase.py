# def jaden(s):
#     if s[0].isalpha():
#         return s[0].upper() + s[1:].lower()
#     else:
#         return s.lower()
    
# def solution(s):
#     return ' '.join(map(jaden, s.split()))

##################################################

def solution(s):
    answer = ''
    flag = True # 앞이 공백이었으면 true
    for idx in range(len(s)):
        if flag and s[idx].isalpha():    # 단어의 첫 문자 & 알파벳임
            s = s[:idx] + s[idx].upper() + s[idx+1:]
            flag = False
            continue
        if s[idx] == ' ':
            flag = True
        else:
            s = s[:idx] + s[idx].lower() + s[idx+1:]
            flag = False
    return s

print(solution("3people unFollowed me"))
print(solution("for the last week"))