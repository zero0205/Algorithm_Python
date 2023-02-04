# n, b = input().split()  # b진법 수 n
# b = int(b)

# num_dict = {chr(65+i):10+i for i in range(26)}

# ans = 0
# l = len(n)
# for i in range(l):
#     if n[i].isalpha():  
#         ans += num_dict[n[i]] * (b ** (l-i-1))
#     else:
#         ans += int(n[i]) * (b ** (l-i-1))
# print(ans)

n, b = input().split()  # b진법 수 n
b = int(b)

num_dict = {chr(65+i):10+i for i in range(26)}

ans = 0
n = n[::-1]
for i in range(len(n)):
    if n[i].isalpha():  
        ans += num_dict[n[i]] * (b ** i)
    else:
        ans += int(n[i]) * (b ** i)
print(ans)