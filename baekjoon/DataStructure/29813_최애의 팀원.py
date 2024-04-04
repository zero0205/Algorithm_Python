from collections import deque

n = int(input())
students = deque([list(input().split()) for _ in range(n)])

while len(students) > 1:
    init, num = students.popleft()
    for _ in range(int(num)-1):
        students.append(students.popleft())
    students.popleft()

print(students[0][0])
