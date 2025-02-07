import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cptis = dict()
for _ in range(n):
    input_cpti = int(input(), 2)
    if input_cpti in cptis:
        cptis[input_cpti] += 1
    else:
        cptis[input_cpti] = 1

answer = 0
for num in cptis.keys():
    answer += (cptis[num]*(cptis[num]-1))//2
    # 1개 다른 사람 세기
    for i in range(m):
        new_num = num ^ (1 << i)
        if new_num > num and new_num in cptis:
            answer += cptis[num] * cptis[new_num]
        # 2개 다른 사람 세기
        for j in range(i+1, m):
            new_num2 = new_num ^ (1 << j)
            if new_num2 > num and new_num2 in cptis:
                answer += cptis[num] * cptis[new_num2]

print(answer)
