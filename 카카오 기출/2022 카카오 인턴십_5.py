from collections import deque

# ShiftRow
def s(arr):
    q = deque(arr)
    tmp = q.pop()
    q.appendleft(tmp)
    return list(q)

# ShiftRow
# def s(arr):
#    q = [arr.pop()]
#    q.extend(arr)
#    return q

# Rotate
def r(arr):
    rn = len(arr)
    cn = len(arr[0])
    x11, x1n, xn1, xnn = arr[0][0], arr[0][cn-1], arr[rn-1][0], arr[rn-1][cn-1]
    # 행 이동
    for i in range(1, cn - 1):
        # 1행 이동
        arr[0][cn-i] = arr[0][cn-i-1]
        # n행 이동
        arr[rn-1][i-1] = arr[rn-1][i]
    # 열 이동
    for j in range(1, rn - 1):
        # 1열 이동
        arr[j-1][0] = arr[j][0]
        # n열 이동
        arr[rn-j][cn-1] = arr[rn-j-1][cn-1]
    arr[0][1] = x11
    arr[1][cn-1] = x1n
    arr[rn-1][cn-2] = xnn
    arr[rn-2][0] = xn1
    return arr

def print_arr(op, arr):
    print(op)
    for r in arr:
        for c in r:
            print(c, end=' ')
        print()

def solution(rc, operations):
    for op in operations:
        if op == "ShiftRow":
            rc = s(rc)
        else:
            rc = r(rc)
        # print_arr(op, rc)
    return rc

##################
def solution2(rc, operations):
    answer = [[]]
    bits = 0
    for i in range(len(operations)):
        if operations[i][0] == 'S':
            bit = 0
        else:
            bit = 1
        bits = bits << 1
        bits += bit
    print(bits)            
    return answer

# 테스트 케이스
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))

# 정답
# [[8, 9, 6], [4, 1, 2], [7, 5, 3]]
# [[8, 3, 3], [4, 9, 7], [3, 8, 6]]
# [[1, 6, 7 ,8], [5, 9, 10, 4], [2, 3, 12, 11]]