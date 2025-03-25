from collections import defaultdict

n = int(input())
nums = [input() for _ in range(n)]
k = int(input())

base36 = [str(x) for x in range(10)]+[chr(x) for x in range(65, 91)]


def decimal_to_base36(num):
    if num == 0:
        return "0"
    result = ""
    while num != 0:
        result = base36[num % 36]+result
        num //= 36
    return result


gap = defaultdict(int)
answer = 0
for i in range(n):
    answer += int(nums[i], 36)
    # nums[i]의 각 자리수와 "Z" 사이의 차이 저장
    for j in range(len(nums[i])):
        ch = nums[i][j]
        if ch != "Z":
            ch_value = int(ch, 36)

            gap[ch] += (35-ch_value)*(36**(len(nums[i])-1-j))

sorted_gap = sorted(gap.items(), key=lambda x: x[1], reverse=True)

for i in range(min(k, len(gap))):
    answer += sorted_gap[i][1]

print(decimal_to_base36(answer))
