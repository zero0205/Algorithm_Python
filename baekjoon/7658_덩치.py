# https://www.acmicpc.net/problem/7568

# 몸무게 x kg, 키 y cm => 덩치 (x,y)
# 몸무게와 키 모두 커야 덩치가 더 큰 것

n = int(input())
arr = []
answer = [1] * n
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(n):
        # 본인이면 지나가기
        if i == j:
            continue
        if (arr[i][0] < arr[j][0]) and (arr[i][1] < arr[j][1]):
            answer[i] += 1
            
for a in answer:
    print(a, end=" ")