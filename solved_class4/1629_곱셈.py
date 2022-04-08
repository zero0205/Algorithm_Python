# https://www.acmicpc.net/problem/1629

a, b, c = map(int, input().split())

def dc(a, b):
    if b == 1:
        return a % c
    else:
        tmp = dc(a, b // 2)
        if b % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c
        
print(dc(a,b))