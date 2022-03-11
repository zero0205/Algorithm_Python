# n 입력받기
n = int(input())
# 배열 생성
arr = [1e9] * 50001
# 제곱수들에 대해 처리
round1 = []
round2 = []
round3 = []
round4 = []
for i in range(1, 224):
    arr[i ** 2] = 1
    round1.append(i ** 2)
# round2
for i in range(len(round1)):
    for j in range(i, len(round1)):
        if round1[i] + round1[j + 1] > 50000:
            break
        arr[round1[i] + round1[j]] = min(2, round1[i] + round1[j])
        

for j in range(1,50001):
    arr[j] = min(arr[j], arr[j - 1] + 1)
    
print(arr[n])