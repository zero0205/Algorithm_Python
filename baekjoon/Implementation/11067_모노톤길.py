import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())

    cafes = {}
    for _ in range(n):
        x, y = map(int, input().split())
        if x not in cafes:
            cafes[x] = []
        cafes[x].append(y)

    prev_y = 0
    counted_cafe = []
    for x, y_list in sorted(cafes.items()):
        y_list.sort()
        if y_list[0] != prev_y:
            y_list.reverse()

        for y in y_list:
            counted_cafe.append([x, y])
        prev_y = y_list[-1]

    m, *arr = list(map(int, input().split()))
    for a in arr:
        print(*counted_cafe[a-1])
