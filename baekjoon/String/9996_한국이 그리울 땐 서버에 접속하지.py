import re

n = int(input())
pattern = re.compile("^"+input().replace("*", "[a-z]*")+"$")

for _ in range(n):
    string = input()
    if pattern.match(string):
        print("DA")
    else:
        print("NE")
