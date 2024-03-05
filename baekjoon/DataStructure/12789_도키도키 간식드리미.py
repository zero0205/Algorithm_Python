n = int(input())
nums = list(map(int, input().split()))

stack = []
cnt = 1
for i in range(n):
    if cnt == nums[i]:  # 순서가 맞는 사람
        cnt += 1
    else:   # 순서 안 맞는 사람
        while stack:    # stack에서 나갈 수 있는 사람 나가기
            if stack[-1] == cnt:
                stack.pop()
                cnt += 1
            else:
                break
        stack.append(nums[i])

# stack에 남은 사람들 중 나올 수 있는 사람
while stack:
    if stack[-1] == cnt:
        stack.pop()
        cnt += 1
    else:
        break

if stack:
    print("Sad")
else:
    print("Nice")
