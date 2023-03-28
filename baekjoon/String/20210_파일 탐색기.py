# import sys
# input = sys.stdin.readline
# from functools import cmp_to_key

# # 문자 비교. 같으면 0, c1이 우선 순위 높으면 1, c2가 우선 순위 높으면 -1
# def str_compare(c1, c2):
#     if c1.lower() == c2.lower():    # Aa, aa, AA와 같은 경우
#         if c1 == c2:    # 둘이 완전히 같음
#             return 0
#         elif c1 < c2:   # c1이 대문자, c2이 소문자
#             return 1
#         else:           # c1이 소문자, c2이 대문자
#             return -1    
#     elif c1.lower() < c2.lower():
#         return 1
#     else:
#         return -1
    
# # 숫자 비교. 같으면 0, n1이 크면 1, n2가 크면 -1   
# def num_compare(n1, n2):
#     if n1 == n2:    # 두 숫자 문자열이 완전히 같은 경우
#         return 0
#     # 두 숫자 길이가 다르고 문자열이 0으로 시작하지 않는 경우
#     if len(n1) < len(n2) and n1[0] != '0' and n2[0] != '0': 
#         return 1
#     elif len(n1) > len(n2) and n1[0] != '0' and n2[0] != '0':
#         return -1
#     # 두 숫자 문자열의 길이가 같은 경우
#     else:
#         num1 = int(n1.replace(0, ''))
#         num2 = int(n2.replace(0, ''))
#         if num1 == num2:
#             return 1 if len(n1) < len(n2) else -1
#         else:
#             return 1 if num1 < num2 else -1
            
# def natural_sort(str1, str2):
#     idx1, idx2 = 0, 0
#     while idx1 < len(str1) or idx2 < len(str2):
#         # 하나는 숫자, 하나는 문자인 경우
#         if str1[idx1].isdigit() and str2[idx2].isalpha():
#             return 1
#         if str1[idx1].isalpha() and str2[idx2].isdigit():
#             return -1
#         # 문자인 경우
#         if str1[idx1].isalpha() and str2[idx2].isalpha():
#             res = str_compare(str1[idx1], str2[idx2])
#             if res == 0:
#                 idx1 += 1
#                 idx2 += 1
#                 continue
#             else:
#                 return res
#         # 숫자인 경우
#         if str1[idx1].isdigit() and str2[idx2].isdigit():
#             n1, n2 = '', ''
#             while str1[idx1].isdigit():
#                 n1 += str1[idx1]
#                 idx1 += 1
#             while str2[idx2].isdigit():
#                 n2 += str1[idx2]
#                 idx2 += 1
#             res = str_compare(n1, n2)
#             if res == 0:
#                 idx1 += 1
#                 idx2 += 1
#                 continue
#             else:
#                 return res

# lst = []
# for _ in range(int(input())):
#     lst.append(input())
    
# print(*sorted(lst, key=cmp_to_key(natural_sort)))
#########################################################
import sys
input = sys.stdin.readline
from functools import cmp_to_key
    
# 문자열 파싱
def parse(str):
    res = []
    i = 0
    while i < len(str):
        if str[i].isalpha():    # 알파벳인 경우
           res.append(str[i]) 
           i += 1
        else:   # 숫자인 경우
            tmp = ''
            while i < len(str) and str[i].isdigit():
                tmp += str[i]
                i += 1
            res.append(tmp)
    return res

def natural_sort(str1, str2):
    lst1 = parse(str1)
    lst2 = parse(str2)
    idx = 0
    while idx < min(len(lst1), len(lst2)):
        if lst1[idx] == lst2[idx]:
            idx += 1
            continue
        # 하나는 숫자, 하나는 문자인 경우
        if lst1[idx].isdigit() and lst2[idx].isalpha():
            return -1
        if lst1[idx].isalpha() and lst2[idx].isdigit():
            return 1
        # 둘 다 문자인 경우
        if lst1[idx].isalpha() and lst2[idx].isalpha():
            if lst1[idx].lower() == lst2[idx].lower():  # 같은 문자이지만 대소문자로 다른 경우
                return 1 if lst1[idx] > lst2[idx] else -1   # 대문자 아스키 코드 < 소문자 아스키 코드
            else:                                       # 다른 문자인 경우
                return 1 if lst1[idx].lower() > lst2[idx].lower() else -1
        # 숫자인 경우
        if lst1[idx].isdigit() and lst2[idx].isdigit():
            if int(lst1[idx]) == int(lst2[idx]):
                return 1 if len(lst1[idx]) > len(lst2[idx]) else -1
            else:
                return 1 if int(lst1[idx]) > int(lst2[idx]) else -1
    return 1 if len(lst1) > len(lst2) else -1
        
lst = []
for _ in range(int(input())):
    lst.append(input().strip())   

for el in sorted(lst, key=cmp_to_key(natural_sort)):
    print(el)