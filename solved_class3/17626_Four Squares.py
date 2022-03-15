# # n 입력받기
# n = int(input())
# # 배열 생성
# arr = [1e9] * 50001
# # 제곱수들에 대해 처리
# round1 = []
# round2 = []
# round3 = []
# # round1
# for i in range(1, 224):
#     arr[i ** 2] = 1
#     round1.append(i ** 2)
# # round2
# for i in range(len(round1)):
#     for j in range(i, len(round1)):
#         if round1[i] + round1[j] > 50000:
#             break
#         arr[round1[i] + round1[j]] = min(2, round1[i] + round1[j])
#         round2.append(round1[i] + round1[j])
        
# # round3
# for i in range(len(round2)):
#     for j in range(i, len(round2)):
#         if round2[i] + round2[j] > 50000:
#             break
#         arr[round2[i] + round2[j]] = min(2, round2[i] + round2[j])
#         round3.append(round2[i] + round2[j])

# # round4
# for i in range(len(round3)):
#     for j in range(i, len(round3)):
#         if round3[i] + round3[j] > 50000:
#             break
#         arr[round3[i] + round3[j]] = min(2, round3[i] + round3[j])
# print(arr[n])

#####################
n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    j = 1
    dp.append(dp[i-1] + 1)
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])