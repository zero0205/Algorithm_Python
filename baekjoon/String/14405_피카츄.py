import re

s = input()

pattern = re.compile(r'^(pi|ka|chu)*$')
if pattern.match(s):
    print("YES")
else:
    print("NO")


# s = input()
# tmp = ""
# ans = "YES"
# for i in range(len(s)):
#     tmp += s[i]
#     if tmp in ["pi", "ka", "chu"]:
#         tmp = ""
#     if len(tmp) >= 3:
#         ans = "NO"
#         break
# print(ans if tmp == "" else "NO")
