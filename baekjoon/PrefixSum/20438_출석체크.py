import sys
input = sys.stdin.readline

# 학생수, 졸고있는학생수, 출석코드 보낼 학생 수, 주어질 구간의 수
# 입장번호는 3 ~ n+2
n, k, q, m = map(int, input().split())
sleeping = [False] * (n+3)
check = [False] * (n+3)
# 졸고 있는 학생들
for num in map(int, input().split()):
    sleeping[num] = True
    
# 출석 코드 전달
def relay(start):
    # 졸고 있는 학생이 출석 코드 받은 경우
    if sleeping[start]:
        return
    # 출석 코드 전달
    for i in range(start, n+3, start):
        if not sleeping[i]:
            check[i] = True # 졸고 있지 않다면 출석
        
# 출석 코드 받을 학생들
for num in map(int, input().split()):
    relay(num)

# 출석되지 않은 학생 수 누적합 구하기
accumulate = [0] * (n+3)
for i in range(3, n+3):
    accumulate[i] = accumulate[i-1] + (0 if check[i] else 1)
 
for _ in range(m):
    start, end = map(int, input().split())
    print(accumulate[end] - accumulate[start-1])