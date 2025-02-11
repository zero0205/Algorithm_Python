# from itertools import combinations

# l, c = map(int, input().split())
# alphabets = set(input().split())

# vowels = alphabets & {"a", "e", "i", "o", "u"}
# constants = alphabets - {"a", "e", "i", "o", "u"}

# answer = []
# for vowel_num in range(1, min(len(vowels)+1, l-2+1)):
#     constant_num = l-vowel_num
#     for vowel_comb in combinations(vowels, vowel_num):
#         for constant_comb in combinations(constants, constant_num):
#             answer.append("".join(sorted(list(vowel_comb+constant_comb))))

# print(*sorted(answer, sep="\n"))

l, c = map(int, input().split())
alphabets = sorted(list(input().split()))


def check_validation(str):
    vowels = {"a", "e", "i", "o", "u"}
    vowel_cnt = 0
    for i in range(len(str)):
        if str[i] in vowels:
            vowel_cnt += 1
    if vowel_cnt >= 1 and len(str)-vowel_cnt >= 2:
        return True
    else:
        return False


def bt(idx, str):
    if len(str) == l:
        if check_validation(str):
            print(str)
        return
    if idx == c:
        return
    # idx번째 문자 포함
    bt(idx+1, str+alphabets[idx])
    # idx번째 문자 포함 X
    bt(idx+1, str)


bt(0, "")
