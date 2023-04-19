switch_num = int(input())
switches = [0] + list(map(int, input().split()))

def toggle(n):
    if switches[n] == 0:
        switches[n] = 1
    else:
        switches[n] = 0
    
def boy(n):
    for i in range(n, switch_num+1, n):
        toggle(i)
        
def girl(n):
    toggle(n)
    for i in range(1, switch_num//2+1):
        if n - i <= 0 or n + i > switch_num:
            break
        if switches[n-i] == switches[n+i]:
            toggle(n-i)
            toggle(n+i)
        else:
            break

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 1:
        boy(b)
    else:
        girl(b)
        
for i in range(1, switch_num+1):
    print(switches[i], end=" ")
    if i % 20  == 0:
        print()