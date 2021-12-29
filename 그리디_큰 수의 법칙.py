# 그리디
# 1. 큰 수의 법칙

n,m,k = map(int, input().split())
lst = list(map(int, input().split()))
cnt=0
sum=0

max1 = max(lst)
lst.remove(max1)

max2 = max(lst)

for j in range(m):
  if cnt < k:
    sum += max1
    cnt+=1
  else:
    sum += max2
    cnt=0

print(sum)