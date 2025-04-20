import sys
input = sys.stdin.readline

INF = int(1e9)


def get_distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2])


n = int(input())
villages = [list(map(int, input().split())) for _ in range(n)]
answer = INF
for center in range(n):
    first = INF
    second = INF
    for neighbor in range(n):
        if center == neighbor:
            continue
        dist = get_distance(villages[center], villages[neighbor])
        if dist < first:
            second = first
            first = dist
        elif dist < second:
            second = dist

    if first+second < answer:
        answer = first+second

print(answer)
