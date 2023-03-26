############ 시간 초과 ############
# def check(str):
#     # 회문인가?
#     if str == str[::-1]:
#         return 0
#     # 유사회문인가?
#     for i in range(len(str)-1):
#         if str[:i] + str[i+1:] == (str[:i] + str[i+1:])[::-1]:
#             return 1
#     # 일반 문자열
#     return 2

# for _ in range(int(input())):
#     print(check(input()))
####################################
def check(s):
    start, end = 0, len(s)-1
    while start <= end:
        # 양쪽 문자가 같은 경우
        if s[start] == s[end]:
            start += 1
            end -= 1
            continue
        # 양쪽 문자가 다른 경우
        else:
            # 오른쪽 문자 제거 시 유사회문인 경우
            if s[:end] + s[end+1:] == (s[:end] + s[end+1:])[::-1]:
                return 1
            # 왼쪽 문자 제거 시 유사회문인 경우
            if s[:start] + s[start+1:] == (s[:start] + s[start+1:])[::-1]:
                return 1
        return 2
    return 0
    
for _ in range(int(input())):
    print(check(input()))
    