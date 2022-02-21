# n 입력받기
n = int(input())
# 이름, 국어, 영어, 수학 점수
student = []
for i in range(n):
    name, kor, eng, math = input().split()
    student.append((int(kor), int(eng), int(math), name))

student.sort(key=lambda x : (-x[0], x[1], -x[2], x[3]))

for s in student:
    print(s[3])