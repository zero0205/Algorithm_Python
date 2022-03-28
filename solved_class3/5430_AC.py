# https://www.acmicpc.net/problem/5430

from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    arr = input().strip()
    if len(arr) == 2:   # 빈 배열이 들어왔을 때
        arr = []
    else:
        arr = arr[1:-1].split(',')
    deq = deque(arr)
    
    rvs = False
    err = False
    
    for cmd in p:
        if cmd == 'R':  # 배열의 순서 뒤집기
            rvs = False if rvs else True
        elif cmd == 'D':   # 첫 번째 수 버리기
            if not deq:
                err = True
                break
            if rvs:
                deq.pop()
            else:
                deq.popleft()
    
    if err:
        print("error")
        continue
    if rvs:
        deq.reverse()
    print("[" + ",".join(deq) + "]")