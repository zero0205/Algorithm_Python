# 그리디
# 4. 곱하기 혹은 더하기

str = input()
result = 0

for i in str:
    if result <= 1 or int(i) <= 1:
        result += int(i)
    else:
        result *= int(i)

print(result)
