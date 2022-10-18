def solution(s):
    stack = 0
    for el in s:
        if el == '(':
            stack += 1
        else:
            if stack <= 0:
                return False
            else:
                stack -= 1
    return True if stack == 0 else False

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))