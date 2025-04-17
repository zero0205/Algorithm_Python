import sys
input = sys.stdin.readline

n, k = map(int, input().split())
students = [input() for _ in range(n)]
window = dict()
answer = 0
for i in range(k+1):
    length = len(students[i])
    if length in window:
        answer += window[length]
    else:
        window[length] = 0
    window[len(students[i])] += 1


for i in range(k+1, n):
    length = len(students[i])
    prev_length = len(students[i-(k+1)])
    window[prev_length] -= 1
    if length in window:
        answer += window[length]
    else:
        window[length] = 0
    window[len(students[i])] += 1

print(answer)
