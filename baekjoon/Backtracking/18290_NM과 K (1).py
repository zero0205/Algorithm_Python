n, m, k = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

ans = -int(1e6)


def bt(lst, lst_sum, idx):
    global ans
    # k개만큼 뽑음
    if len(lst) == k:
        ans = max(ans, lst_sum)
        return
    for i in range(idx+1, n*m):
        # lst에 있는 칸들과 인접하지 않으면 재귀
        neighbor = False
        for j in lst:
            # 같은 행 인접
            if i//m == j//m and abs(i-j) == 1:
                neighbor = True
                break
            # 같은 열 인접
            if i % m == j % m and abs(i-j) == m:
                neighbor = True
                break
        if not neighbor:
            bt(lst+[i], lst_sum+board[i//m][i % m], i)


bt([], 0, -1)
print(ans)
