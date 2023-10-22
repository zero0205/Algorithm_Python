def solution(pos, monitors, move):
    answer = []
    pn, px, py = pos
    for x, y in move:
        # 상하 이동
        if x == 0:
            py += y
            if py < 0:
                py = 0
            if py > monitors[pn][1]:
                py = monitors[pn][1]-1
        # 좌우 이동
        else:
            px += x
            # 같은 모니터 내에서 이동
            if 0 <= px < monitors[pn][0]:
                continue
            # 왼쪽 모니터로 이동
            elif px < 0:
                for num in range(pn-1, -1, -1):
                    px += monitors[num][0]
                    # 이동한 모니터 세로가 작음
                    if monitors[num][1] < py:
                        py = monitors[num][1] - 1
                    if px > 0:
                        pn = num
                        break
            # 오른쪽 모니터로 이동
            else:
                for num in range(pn+1, len(monitors), 1):
                    px -= monitors[num][0]
                    # 이동한 모니터 세로가 작음
                    if monitors[num][1] < py:
                        py = monitors[num][1] - 1
                    if px < monitors[num][0]:
                        pn = num
                        break
    return [pn, px, py]
