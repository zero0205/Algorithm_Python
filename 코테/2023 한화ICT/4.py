import sys
sys.setrecursionlimit(10**5)
from heapq import heappop, heappush

disappear = dict()

def dfs(msg, cnt):
    if len(msg) == 0:
        return
    if len(msg) == 1:
        if msg in disappear:
            disappear[msg] = max(disappear[msg], cnt)
        else:
            disappear[msg] = cnt
        return
    pivot = msg[0]  # 첫번째 문자가 기준
    arr = msg.split(pivot)
    flag = False
    for a in arr:
        if pivot in a:
            flag = True
        dfs(a, cnt+1)
    if not flag:    # pivot이 사라짐
        if pivot in disappear:
            disappear[pivot] = max(disappear[pivot], cnt)
        else:
            disappear[pivot] = cnt
    return

def solution(message):
    answer = ''
    dfs(message, 0)  
    q = []
    for k, v in disappear.items():
        heappush(q, (v, k))
    while q:
        answer += heappop(q)[1]
    return answer