from copy import deepcopy

n = int(input())
x = sorted(list(map(int, input().split())))
answer = []
arr = [-1]*(2*n)


def bt(idx):
    if idx == n:
        new_arr = deepcopy(arr)
        answer.append(new_arr)
        return
    for i in range(2*n-x[idx]-1):
        if arr[i] == -1 and arr[i+x[idx]+1] == -1:
            arr[i] = x[idx]
            arr[i+x[idx]+1] = x[idx]
            bt(idx+1)
            arr[i] = -1
            arr[i+x[idx]+1] = -1


bt(0)
if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    print(*answer[0])
