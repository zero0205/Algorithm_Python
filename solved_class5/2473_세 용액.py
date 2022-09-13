######### PyPy3¸¸ Åë°ú ##########
n = int(input())
arr = sorted(list(map(int, input().split())))

ans = []
ans_sum = int(1e9) * 3

for a in range(n-2):
    b = a + 1
    c = n - 1
    while b < c:
        s = arr[a] + arr[b] + arr[c]
        if abs(s) <= abs(ans_sum):
            ans = [arr[a], arr[b], arr[c]]
            ans_sum = s        
        if s == 0:
            break
        elif s < 0:
            b += 1
        else:
            c -= 1
    
print(" ".join(map(str, ans)))