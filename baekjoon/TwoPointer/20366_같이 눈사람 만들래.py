n = int(input())
diameter = sorted(list(map(int, input().split())))
ans = int(1e9)
 
# 두 눈사람의 키차이 : (1,4)-(2,3)
# 큰 눈사람 고정
for s in range(n-3):
    for e in range(s+3, n):
        l, r = s+1, e-1
        while l <= r:
            diff = (diameter[s]+diameter[e])-(diameter[l]+diameter[r])
            if diff == 0:
                print(0)
                exit()
            elif diff > 0:
                l += 1
            else:
                r -= 1
            if abs(diff) < ans:
                ans = abs(diff)
            
print(ans)