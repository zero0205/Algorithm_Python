n = int(input())

def triangle(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    tmp = triangle(n//2)
    res = []
    
    for t in tmp:
        res.append(' '*(n//2) + t + ' '*(n//2))
    for t in tmp:
        res.append(t + ' ' + t)
    return res

print('\n'.join(triangle(n)))