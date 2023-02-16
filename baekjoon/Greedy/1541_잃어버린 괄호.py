# exp = input()

# tmp = ''
# flag = False
# for i in range(len(exp)):
#     if exp[i].isdigit():
#         if exp[i] == '0':
#             if not tmp:
#                 continue
#             if not tmp[-1].isdigit():
#                 continue
#         tmp += exp[i]
#     else:
#         if exp[i] == '-':   # -인 경우
#             if not flag:    # 괄호가 열리지 않은 상태
#                 tmp += '-('
#                 flag = True
#             else:           # 앞에서 괄호가 열린 상태
#                 tmp += ')-'
#                 flag = False
#         else:               # +인 경우
#             tmp += '+'
# if flag:
#     tmp += ')'
    
# print(eval(tmp))
####################################################
exp = input().split('-')

ans = eval(exp[0])
if len(exp) > 1:
    for e in exp[1:]:
        ans -= eval(e)
print(ans)
####################################################
# exp = input().split('-')    # - 기준으로 잘라줌

# def calculate(exp):
#     res = 0
#     tmp = 0
#     for c in exp:
#         if c.isdecimal():
#             tmp *= 10
#             tmp += int(c)
#         else:   # +인 경우
#             res += tmp
#             tmp = 0
#     if tmp != 0:
#         res += tmp
#     return res

# if len(exp) == 1:
#     print(calculate(exp[0]))
#     exit()
    
# ans = calculate(exp[0])
# for e in exp[1:]:
#     ans -= calculate(e)
    
# print(ans)