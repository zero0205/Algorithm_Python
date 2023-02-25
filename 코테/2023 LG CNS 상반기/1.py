def get_distance(x, y, square):
    min_dist = 2000
    for sx, sy in square:
        # 직선경로로 지하철에 도달 가능
        if square[0][0] <= x <= square[1][0]:   # 세로 경로
            min_dist = min(min_dist, abs(sy-y))
        if square[0][1] <= y <= square[3][1]:   # 가로 경로
            min_dist = min(min_dist, abs(sx-x))
        # 순환선 꼭짓점으로 가기
        min_dist = min(abs(sx-x)+abs(sy-y), min_dist)
    return min_dist

def solution(ax, ay, bx, by, square):
    # 지하철 이용하는 경우
    answer = get_distance(ax,ay,square)+get_distance(bx, by, square)
    # 지하철 이용 안 하는 경우
    answer = min(answer, abs(ax-bx)+abs(ay-by))
    return answer