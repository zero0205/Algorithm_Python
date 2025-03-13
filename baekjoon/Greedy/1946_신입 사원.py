from heapq import heappop, heappush
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    applicants = []
    for _ in range(n):
        doc, interview = map(int, input().split())
        heappush(applicants, (doc, interview))

    answer = 1
    comp_interview = heappop(applicants)[1]
    while applicants:
        now = heappop(applicants)
        if now[1] < comp_interview:
            comp_interview = now[1]
            answer += 1
    print(answer)
