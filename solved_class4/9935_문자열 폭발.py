# https://www.acmicpc.net/problem/9935
################# replace 이용 ###################
# import re

# s = input()
# explosion = input()

# ex_len = len(explosion)

# while True:
#     if explosion not in s:
#         break
#     s = s.replace(explosion, "")

# if s:
#     print(s) 
# else:
#     print("FRULA")
################# split 이용 ###################
# s = input()
# e = input()

# while True:
#     s_arr = s.split(e)
#     if len(s_arr) <= 1:
#         break
#     else:
#         s = ''
#         for i in s_arr:
#             s += i
            
# if s:
#     print(s)
# else:
#     print("FRULA")
############################################# 
s = input()
e = input()

e_last = e[-1]  # 폭발 문자열 마지막 글자
stack = []
e_len = len(e)

for c in s:
    stack.append(c)
    # 스택에 방금 들어간 문자가 폭발 문자열의 마지막 글자와 일치할때
    # 스택의 top에서부터 폭발 문자열과 일치하는지 확인
    if c == e_last and "".join(stack[-e_len:]) == e:
        del stack[-e_len:]
# 다 끝나고 스택에 남은 글자들을 문자열로 합쳐줌
ans = "".join(stack)

if ans:
    print(ans)
else:
    print("FRULA")