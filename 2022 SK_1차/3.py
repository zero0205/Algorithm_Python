from math import factorial

def count_path(x,y, end_x, end_y):  # (x,y)에서 (end_x, end_y)로 가는 경로의 수 개수 구하기
    a = end_x - x
    b = end_y - y
    return factorial(a + b) // (factorial(a) * factorial(b))  # 조합

def solution(width, height, diagonals):
    answer = 0
    # 각 대각선을 이용하는 모든 경우에 대해 구하기
    for d in diagonals:
        # 처음 오른 아래로 갈 때
        answer += count_path(0, 0, d[0], d[1] - 1) * count_path(d[0] - 1, d[1], width, height)
        # 처음 왼 위로 갈 때
        answer += count_path(0, 0, d[0] - 1, d[1]) * count_path(d[0], d[1] - 1, width, height)
        answer %= 10000019
    return answer

# 넓이, 높이 입력
width, height = map(int, input().split())
# 대각선 개수 입력 
d = int(input())
# 대각선 정보 입력
diagonals = []
for _ in range(d):
    diagonals.append(list(map(int, input().split())))
    
print(solution(width, height, diagonals))