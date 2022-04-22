from copy import deepcopy
# from os import remove
# import re

# def solution(call):
#   answer = call
#   call = call.lower()
#   possible = {} #O(1)
#   for i in range(1,len(call)+1):
#     for j in range(len(call)-i+1):
#       string = call[j:j+i]
#       if string in possible:
#         possible[string] += 1
#       else:
#         possible[string] = 1
        
#   print(possible)
        
#   removes = []
#   max_value = 0
#   for i in possible.keys():
#     if max_value < possible[i]:
#       removes.clear()
#       removes.append(i)
#       max_value = possible[i]
#     elif max_value == possible[i]:
#       removes.append(i)
      
#   removesIndex = []
#   for i in removes:
#     p = re.compile(i)
#     m = p.finditer(call)
#     for r in m: 
#       start, end = r.span()
#       print(start,end)
#       removesIndex.append(answer[start:end])
#   for i in removesIndex:
#     answer = answer.replace(i, "")
      
#   return answer

def solution(call):
  answer = ""
  n = len(call)
  count = [0]*27
  copy_call = deepcopy(call)
  call = call.lower()
  for char in call:
    count[ord(char)-ord('a')] += 1
  
  max_value = max(count)
  remove_alpha = set()
  remove_index = [0]*n
  for i in range(len(count)):
    if count[i] == max_value:
      remove_alpha.add(chr(ord('a')+i))
      
  for i in range(n):
    if call[i] in remove_alpha:
      remove_index[i] = 1
      
  for i in range(n):
    if remove_index[i] == 0:
      answer += copy_call[i]
      
  return answer
        

print(solution("ABCabcA"))