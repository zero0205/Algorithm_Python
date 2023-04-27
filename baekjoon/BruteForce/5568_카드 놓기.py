from itertools import permutations

n = int(input())
k = int(input())
cards = []
for _ in range(n):
    cards.append(input())
    
nums = set()
for arr in list(permutations(cards, k)):
    nums.add(int(''.join(arr)))
print(len(nums))