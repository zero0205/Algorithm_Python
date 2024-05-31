s = input()


def is_palindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True


for i in range(len(s)):
    new_s = s+(s[:i])[::-1]
    if is_palindrome(new_s):
        print(len(new_s))
        break
