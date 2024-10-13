n = int(input())
ans = 0

while n:
    str_n = str(n)
    ans += str_n.count("1")
    n = int("0"+str_n.replace("1", ""))
    
    if n:
        n -= 1
        ans += 1
print(ans)