import re

def check(s):
    p = re.compile('^[A-F]{,1}A+F+C+[A-F]{,1}$')
    res = p.match(s)
    return "Good" if res == None else "Infected!"
    
for _ in range(int(input())):
    print(check(input()))