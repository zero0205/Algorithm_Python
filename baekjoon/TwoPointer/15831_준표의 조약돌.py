n, b, w = map(int, input().split())
pebbles = input()

answer = 0
left, right = 0, 0
count = dict([("B", 0), ("W", 0)])
count[pebbles[left]] += 1
while right < n:
    if count["B"] <= b and count['W'] >= w:
        answer = max(answer, right-left+1)
    right += 1
    if right > n-1:
        break
    count[pebbles[right]] += 1
    while count['B'] > b:
        count[pebbles[left]] -= 1
        left += 1

print(answer)
