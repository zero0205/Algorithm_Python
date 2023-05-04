n = int(input())
arr = list(map(int, input().split()))
ops = list(map(int, input().split()))

min_v = int(1e9)
max_v = -int(1e9)

# 연산
def calc(op, a, b):
    if op == 0:     # 더하기
        return a+b
    elif op == 1:   # 빼기
        return a-b
    elif op == 2:   # 곱하기
        return a*b
    elif op == 3:   # 나누기
        if a < 0:
            return -(-a//b)
        else:
            return a//b

def dfs(res, idx):
    global min_v, max_v
    if idx == n:
        min_v = min(min_v, res)
        max_v = max(max_v, res)
        return 
    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            dfs(calc(i, res, arr[idx]), idx+1)
            ops[i] += 1
        
dfs(arr[0], 1)

print(max_v)
print(min_v)