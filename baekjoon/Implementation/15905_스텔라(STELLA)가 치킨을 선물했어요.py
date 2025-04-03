n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (-x[0], x[1]))

answer = 0
for i in range(5, n):
    if arr[i][0] == arr[4][0]:
        answer += 1
    else:
        break

print(answer)
