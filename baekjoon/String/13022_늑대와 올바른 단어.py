word = input()
wolf = set(['w'*i+'o'*i+'l'*i+'f'*i for i in range(1, 13)])
    
# 첫 글자가 w가 아니거나 단어 길이가 4의 배수가 아니라면 올바르지 않은 단어
if word[0] != 'w' or len(word) % 4 != 0:
    print(0)
    exit()
    
start = 0
while True:
    end = start + 1
    if end >= len(word):
        break
    # w들 스킵
    while word[end] == 'w':
        end += 1
        if end >= len(word): # w가 단어의 끝에 나온다는 건 올바르지 않은 단어
            print(0)
            exit()
    # 다음 단어 나올 때까지
    while word[end] != 'w':
        end += 1
        if end >= len(word):
            break
    # 1번 규칙으로 만든 올바른 단어인지 확인
    if word[start:end] not in wolf:
        print(0)
        exit()
    start = end
print(1)