croatia_alphabet = set(["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="])

input_str = input()
n = len(input_str)
answer = 0
idx = 0
while idx < n:
    answer += 1
    if idx >= n-1:
        break
    if idx < n-1 and input_str[idx:idx+2] in croatia_alphabet:
        idx += 2
        continue
    elif idx < n-2 and input_str[idx:idx+3] == "dz=":
        idx += 3
        continue
    idx += 1
print(answer)
