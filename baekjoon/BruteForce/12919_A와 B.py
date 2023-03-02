from collections import deque

s = input()
t = input()

# s_num = 0
# for i in range(len(s)):
#     if s[i] == 'A': # A는 0, B는 1
        
def flip(str):
    res = ''
    for i in range(len(str)):
        if str[i] == 'A':
            res += 'B'
        else:
            res += 'A'
    return res

q = deque([s])

while q:
    now = q.popleft() 
    if now == t:
        print(1)
        exit()
    if len(now) >= len(t):
        continue
    # A 추가
    q.append(now+'A')
    # B 추가하고 뒤집기
    q.append((now+'B'))
print(0)