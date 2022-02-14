# 문자열 입력받기
arr = input()

res = int(arr[0])
# 1. 왼쪽에서부터 온 숫자가 0 또는 1 이라면 더하기, 아니면 곱하기 넣기
# 2. 곱하려는데 2번째 피연산자가 0 또는 1이라면 더하기
for i in arr[1:]:
    num = int(i)
    if res == 0 or res == 1:
        res += num
    else : 
        if num == 0 or num==1:
            res += num
        else:
            res *= num
        
# 결과값 출력
print(res)

###### 위의 코드를 좀 더 간결하게 줄이면 ######
# 문자열 입력받기
# arr = input()

# res = int(arr[0])

# for i in arr[1:]:
#     num = int(i)
#     if res <= 1 or num <= 1:
#         res += num
#     else:
#         res *= num
        
# # 결과값 출력
# print(res)