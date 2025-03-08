from collections import defaultdict

n = int(input())
nums_dict = defaultdict(int)
for _ in range(n):
    nums_dict[int(input())] += 1

sorted_nums = sorted(nums_dict.items(), key=lambda x: (-x[1], x[0]))
print(sorted_nums[0][0])
