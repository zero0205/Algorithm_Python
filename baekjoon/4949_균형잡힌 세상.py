# https://www.acmicpc.net/problem/4949

from collections import deque

def is_balance():
    q = []
    for c in input():
        if c == '.':
            print("yes")
            break
        if c == '[':
            q.append('[')
        elif c == ']':
            if not q or q.pop() != '[':
                print("no")
                break
        elif c == '(':
            q.append('(')
        elif c == ')':
            if not q or q.pop() != '(':
                print("no")
                break
        else:
            continue
        
while True:
    try:
        is_balance()
    except EOFError:
        break