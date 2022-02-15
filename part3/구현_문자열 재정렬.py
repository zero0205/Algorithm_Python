# 문자열 입력받기
s = list(input())
s.sort()    # 정렬되면 숫자, 대문자 순서

number = []
answer = ""

for i in s:
    if i.isdecimal():
        number.append(int(i))
    else:
        answer += i
        
# 모든 숫자 더한 값 붙이기
answer += str(sum(number))
    
print(answer)