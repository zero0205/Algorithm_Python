word = input()

ans = 0


def vowel(c):
    if c in ['A', 'E', 'I', 'O', 'U']:
        return True
    return False


def bt(idx, word, nums):
    global ans
    if idx == len(word):
        # L을 포함하는 즐거운 단어인 경우
        if 'L' in word:
            ans += (5**nums[0])*(20**nums[1])
        return
    # word[idx]가 '_'인 경우
    if word[idx] == '_':
        # 모음
        if idx < 2 or not (vowel(word[idx-2]) and vowel(word[idx-1])):
            new_word = word[:idx]+'A'+word[idx+1:]
            bt(idx+1, new_word, [nums[0]+1, nums[1]])
        # 자음
        if idx < 2 or (vowel(word[idx-2]) or vowel(word[idx-1])):
            new_word = word[:idx]+'B'+word[idx+1:]
            bt(idx+1, new_word, [nums[0], nums[1]+1])
        # L
        if idx < 2 or (vowel(word[idx-2]) or vowel(word[idx-1])):
            new_word = word[:idx]+'L'+word[idx+1:]
            bt(idx+1, new_word, nums)
    else:
        # idx까지의 문자열이 모음 또는 자음이 3번 반복되지는 않는지
        if idx >= 2:
            if vowel(word[idx-2]) and vowel(word[idx-1]) and vowel(word[idx]):
                return
            if not (vowel(word[idx-2]) or vowel(word[idx-1]) or vowel(word[idx])):
                return
        bt(idx+1, word, nums)


bt(0, word, [0, 0])
print(ans)
