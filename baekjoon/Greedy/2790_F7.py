import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]

scores.sort(reverse=True)
cutline = scores[0]+1
answer = 1

for i in range(1, n):
    possible_max_score = scores[i]+n
    if cutline > possible_max_score:
        break

    cutline = max(cutline, scores[i]+i+1)
    answer += 1
print(answer)
