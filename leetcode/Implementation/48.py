from copy import deepcopy


def rotate(matrix):
    n = len(matrix)
    max_depth = n//2
    for depth in range(max_depth+1):
        length = n-depth*2-1
        # 위쪽 저장
        top = deepcopy(matrix[depth][depth+1:n-depth])
        # 왼 -> 위
        for i in range(length):
            matrix[depth][n-1-depth-i] = matrix[depth+i][depth]
        # 아래 -> 왼
        for i in range(length):
            matrix[depth+i][depth] = matrix[n-1-depth][depth+i]
        # 오른 -> 아래
        for i in range(length):
            matrix[n-1-depth][depth+i] = matrix[n-1-depth-i][n-1-depth]
        # 위 -> 오른
        for i in range(length):
            matrix[n-1-depth-i][n-1-depth] = top[length-1-i]


rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
