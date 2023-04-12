import sys
input = sys.stdin.readline

n, m = map(int, input().split())
people = [[0] * (m+1) for _ in range(n+1)]  # (1,1)부터 사람 수 누적합
for i in range(1, n+1):
    arr = [0] + list(map(int, input().split()))
    for j in range(1, m+1):
        people[i][j] = people[i-1][j] + people[i][j-1] - people[i-1][j-1] + arr[j]
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    print(people[x2][y2] - people[x1-1][y2] - people[x2][y1-1] + people[x1-1][y1-1])