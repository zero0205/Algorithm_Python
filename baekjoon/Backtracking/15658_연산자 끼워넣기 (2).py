n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))    # 덧셈, 뺄셈, 곱셈, 나눗셈 개수

min_ans, max_ans = int(1e9), -int(1e9)


def bt(idx, total):
    global min_ans, max_ans
    if idx == n:
        min_ans = min(min_ans, total)
        max_ans = max(max_ans, total)
        return
    # 덧셈
    if op[0] > 0:
        op[0] -= 1
        bt(idx+1, total+arr[idx])
        op[0] += 1
    # 뺄셈
    if op[1] > 0:
        op[1] -= 1
        bt(idx+1, total-arr[idx])
        op[1] += 1
    # 곱셈
    if op[2] > 0:
        op[2] -= 1
        bt(idx+1, total*arr[idx])
        op[2] += 1
    # 나눗셈
    if op[3] > 0:
        op[3] -= 1
        bt(idx+1, int(total/arr[idx]))
        op[3] += 1


bt(1, arr[0])
print(max_ans)
print(min_ans)
