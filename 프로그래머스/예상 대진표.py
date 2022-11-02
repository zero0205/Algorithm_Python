# import math

# def solution(n,a,b):
#     answer = 1

#     if a > b:
#         a,b = b, a 
        
#     for _ in range(int(math.sqrt(n))):
#         if b-a==1 and a%2==1:
#             break
#         a = math.ceil(a/2)
#         b = math.ceil(b/2)
#         answer += 1

#     return answer

##################################################
import math

def next_num(n):
    if n % 2 == 1:
        return (n+1) // 2
    else:
        return n // 2

def solution(n,a,b):
    answer = 1
    if a > b:
        a,b = b, a 

    for _ in range(int(math.sqrt(n))):
        if a % 2 == 1 and b - a == 1:
            break
        a = next_num(a)
        b = next_num(b)
        answer += 1
    return answer

print(solution(8,4,7))