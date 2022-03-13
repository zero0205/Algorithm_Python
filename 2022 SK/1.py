# def solution(money, costs):
#     # money : 공장이 생산해야 하는 금액
#     # costs : 6종류 동전의 생산 단가를 나타내는 1차원 정수 배열(1,5,10,50,100,500)
#     answer = 0
#     # DP
#     dp = [int(1e9)] * 1000001
#     dp[0] = 0
#     money_type = [1,5,10,50,100,500]
#     for i in range(6):
#         for j in range(money_type[i], money + 1):
#             if dp[j - money_type[i]] != int(1e9):
#                 dp[j] = min(dp[j], dp[j - money_type[i]] + costs[i])

#     return dp[money]

########################
# 그리디
def solution(money, costs):
    answer = 0
    money_arr = [1,5,10,50,100,500]
    rate = []
    for i in range(6):
        rate.append((costs[i] / money_arr[i], money_arr[i], costs[i]))
    rate.sort()
    
    for r in rate:
        if money == 0:
            break
        num = money // r[1]
        answer += num * r[2]
        money %= r[1]
        # print(f"money : {r[1]}, num : {num}")
    return answer

# money 입력받기
m = int(input())
# costs 입력받기
costs = list(map(int, input().split()))

print(solution(m, costs))

####### test case #######
### example 1 ####
# 4578
# 1 4 99 35 50 1000
# answer : 2308

### example 2 ####
# 1999
# 2 11 20 100 200 600
# answer : 2798