import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
students = []
num_cnt = defaultdict(int)
for _ in range(n):
    input_value = int(input())
    students.append(input_value)
    num_cnt[input_value] += 1

maximum_value = max(students)

count = [0]*(maximum_value+1)
for k, v in sorted(num_cnt.items()):
    count[k] += v-1
    for i in range(k*2, maximum_value+1, k):
        count[i] += v

answer = []
for i in range(n):
    answer.append(count[students[i]])

print(*answer, sep="\n")
