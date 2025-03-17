def countAndSay(n):
    string = "1"
    for _ in range(n-1):
        new_string = ""
        cnt = 1
        prev = string[0]
        for s in string[1:]:
            if s == prev:
                cnt += 1
            else:
                new_string += (str(cnt)+prev)
                prev = s
                cnt = 1
        new_string += (str(cnt)+prev)
        string = new_string
    return string


print(countAndSay(1))
print(countAndSay(4))
