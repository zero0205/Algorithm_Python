# import re

# def find_state(string, parent):
#   if string[0] == '{' and string[-1] == '}':
#     if string[1:-1] not in parent:
#       return string[1:-1]
#     return find_state(parent[string[1:-1]], parent)
#   return parent[string]
# def solution(tstring, variables):
#   answer = ''
#   parent = {}
#   graph = {}
#   for i in variables:
#     parent[i[0]] = i[1]
    
#   for a, b in variables:
#     if b[0] == '{' and b[-1] == '}':
#       graph[a] = b
#       graph[b] = b[1:-1]
#     else:
#       graph[a] = b
#   print(graph)
  
#   # p = re.compile("\{[a-z]+\}")
#   # m = p.findall(tstring)
#   # print(tstring)
#   # print(m)
    
#   return answer

from collections import defaultdict
import re

rules = dict()
outEdges = defaultdict(list)

def dfs(current, changed):
  rules[current] = changed
  for next in outEdges[current]:
    dfs(next, changed)
    
def is_variable(value, variables):
    return value[0] == '{' and value[-1] == '}' and value[1: -1] in variables  # O(1)
    
def set_state(key, variables):
  if is_variable(key, variables):
    converted = rules[key[1:-1]]
    if is_variable(converted, variables):
      return key
    else:
      return converted
  else:
    return key

def solution(tstring, variables):
  for i in variables:
    rules[i[0]] = i[1]
  variables = set(var[0] for var in variables)
  start_vars = []
  for key, value in rules.items():
    if is_variable(value, variables):
      outEdges[value[1:-1]].append(key)
    else:
      start_vars.append(key)
  
  for var in start_vars:
    dfs(var, rules[var])
  
  p = re.compile('\{[a-z]+\}')
  m = p.findall(tstring)
  replace_state = dict()
  for string in m:
    if string not in replace_state:
      replace_state[string] = set_state(string, variables) 
  
  for key, value in replace_state.items():
    tstring = tstring.replace(key, value)
  print(tstring)
  return tstring
      

# solution("this is {template} {template} is {state}",[["template", "{state}"], ["state", "{templates}"]])
# solution("{a} {b} {c} {d} {i}",[["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]])
solution("this is {template} {template} is {state}",[["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]])
