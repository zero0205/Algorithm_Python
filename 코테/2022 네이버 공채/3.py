# 파란 격자들의 좌표 구하기
def get_blue(points):
    res = []
    # 도형에 들어가는 격자들 좌표 구하기
    arr = set()
    for i in range(len(points)):
        next = i + 1 if ((i + 1) < len(points)) else 0
        # 세로 일직선
        if points[i][1] == points[next][1]: 
            for j in range(i, next):
                arr.add([j, points[i][1]])
        # 위로 대각선
        elif points[i][0] >= points[next][0]:
            while 
    return res

def solution(hax_grid, points):
    answer = -1
    get_blue(points)
    return answer
