n = int(input())

array = []

for i in range(n):
  name, score = input().split()
  score = int(score)
  array.append((name, score))

array.sort(key = lambda x : x[1])

for j in array:
  print(j[0], end = ' ')