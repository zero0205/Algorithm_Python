n = int(input())
m = int(input())
ingredients = list(map(int, input().split()))

ingredients.sort()

l, r = 0, n-1
answer = 0
while l < r:
    if ingredients[l]+ingredients[r] == m:
        answer += 1
        l += 1
        r -= 1
    elif ingredients[l]+ingredients[r] < m:
        l += 1
    else:
        r -= 1
print(answer)
