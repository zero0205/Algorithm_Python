# k = int(input())
# ans = 0
# length = 1

# def make_arr(k):
#     global ans, length
#     if length >= k:
#         return
#     ans = (ans << length) | (ans ^ (2**length-1))
#     length *= 2
#     make_arr(k)
    
# make_arr(k)
# print(ans & (1 << (length-k)))
#######################################
# k = int(input())
# ans = 0
# length = 1

# while True:
#     if length >= k:
#         break
#     ans = (ans << length) | (ans ^ (2**length-1))
#     length *= 2

# print(ans & (1 << (length-k)))
#######################################
# 투에-모스 수열 점화식 이용
k = int(input())

def func(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num % 2 == 0:
        return func(num//2)
    else:
        return 1 - func(num//2)
    
print(func(k-1))