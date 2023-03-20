########## 시간 초과 ##########
# s = input()
# t = input()

# def dfs(x):
#     if len(x) == len(t):
#         if x == t:
#             print(1)
#             exit()
#         else:
#             return
#     dfs(x+'A')
#     dfs((x+'B')[::-1])
#     return

# dfs(s)
# print(0)

#######################
s = input()
t = input()

def dfs(x):
    if len(x) == len(s):
        if x == s:
            print(1)
            exit()
        else:
            return
    if x[-1] == 'A':
        dfs(x[:-1])
    if x[0] == 'B':
        dfs(x[::-1][:-1])
    return
        
dfs(t)
print(0)