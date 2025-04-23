import sys
input = sys.stdin.readline

n = int(input())
answer = 0
buffer = 0
for _ in range(n):
    d, v = map(int, input().split())
    buffer += v  # 이번 조각을 다운하는데 걸리는 시간
    if buffer > 0:
        answer += buffer    # 지연 시간 추가
        buffer = 0
    buffer -= d  # 다운로드에 필요한 시간에서 재생된 시간 빼기
print(answer)
