from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
delivery = []
for _ in range(int(input())):
    send, receive, num = map(int, input().split())
    heappush(delivery, (receive, send, num))

ans = 0
truck = [0] * n   # i->(i+1)번째 마을로 갈 때 트럭에 싣는 박스 수
while delivery:
    receive, send, num = heappop(delivery)
    possible_box = num
    for i in range(send, receive):
        if truck[i]+num > c:  # 용량 초과
            possible_box = min(possible_box, c-truck[i])
    for i in range(send, receive):  # 트럭에 가능한만큼 싣기
        truck[i] += possible_box
    ans += possible_box
print(ans)
