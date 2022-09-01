sudoku = [list(map(int,input())) for _ in range(9)]
# 빈칸 저장
emp = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            emp.append((i, j))

# 3X3 사각형 체크
def chk_3X3(x, y, num):
    r = (x // 3) * 3
    c = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[r+i][c+j] == num: # 겹치는 번호 있으면 return False
                return False
    return True

# 가로줄 체크
def chk_row(x, y, num):
    for i in range(9):
        if sudoku[x][i] == num:
            return False
    return True

# 세로줄 체크
def chk_col(x, y, num):
    for i in range(9):
        if sudoku[i][y] == num:
            return False
    return True

def dfs(cnt):
    if cnt == len(emp):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end="")
            print()
        exit() 
        
    r, c = emp[cnt]
    for k in range(1, 10):
        if chk_3X3(r, c, k) and chk_col(r, c, k) and chk_row(r, c, k):
            sudoku[r][c] = k
            dfs(cnt + 1)
            sudoku[r][c] = 0       
              
dfs(0)