# def solution(s):
#     l = len(s)
#     idx = 0
#     prev = s[0]
#     while True:
#         idx += 1
#         print(idx, s)
#         if idx >= l:
#             return 0
#         if prev == s[idx]:
#             if l == 2:
#                 return 1
#             else:
#                 s = s[:idx-1] + s[idx+1:]
#                 idx = 0
#                 l -= 2
#                 prev = s[0]
#         else:
#             prev = s[idx]      
              
##################################
def solution(s):
    if len(s) % 2 == 1:
        return 0
    stack = [s[0]]
    for i in s[1:]:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return 0 if stack else 1
              
print(solution("baabaa"))
print(solution("cdcd"))