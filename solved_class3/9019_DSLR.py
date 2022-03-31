# https://www.acmicpc.net/problem/9019

from collections import deque
import sys
input = sys.stdin.readline

def D(n):
    return (n * 2) % 10000

def S(n):
   return (n - 1) % 10000
    
def L(n):
    d1 = n // 1000
    n %= 1000
    return n * 10 + d1

def R(n):
    d4 = n % 10
    return n // 10 + d4 * 1000

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    q = deque([(a, "")])
    visited = [False] * 10000
    visited[a] = True
    while q:
        n, s = q.popleft()
        if n == b:
            print(s)
            break
        
        nx = D(n)
        if not visited[nx]:
            q.append((nx, s + 'D'))
            visited[nx] = True
        nx = S(n)
        if not visited[nx]:
            q.append((nx, s + 'S'))
            visited[nx] = True
        nx = L(n)
        if not visited[nx]:
            q.append((nx, s + 'L'))
            visited[nx] = True
        nx = R(n)
        if not visited[nx]:
            q.append((nx, s + 'R'))
            visited[nx] = True