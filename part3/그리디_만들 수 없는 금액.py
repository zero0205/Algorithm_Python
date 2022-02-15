# import itertools

# # 동전의 개수 입력받기
# n = int(input())
# # 동전 종류 입력받기
# coin = list(map(int, input().split()))
# coin.sort()

# # 만들어질 수 있는 최대 금액 크기만큼의 배열을 만듦
# # 만들어질 수 있는 금액이면 True
# is_possible = [False] * (sum(coin) + 1)
# is_found = False

# for i in range(1, n + 1):
#     if is_found:
#         break
#     comb = list(itertools.combinations(coin, i))
#     max = sum(comb.pop())   # 오름차순으로 정렬해둬서 가장 뒤의 원소들의 합이 가장 클 것
#     # 만들 수 있는 금액들 체크
#     for j in comb:
#         is_possible[sum(j)] = True
        
#     # 이제 is_possible 배열에서 1~max까지의 값 중 False인 값이 있다면 그거는 못 만드는거
#     for k in range(1, max + 1):
#         if not is_possible[k]:
#             is_found = True
#             answer = k
    
# print(k)

# 동전의 개수 입력받기
n = int(input())
# 동전 종류 입력받기
coin = list(map(int, input().split()))
coin.sort()

target = 1
for i in coin:
    if target < i:
        break
    target += i
    
print(target)