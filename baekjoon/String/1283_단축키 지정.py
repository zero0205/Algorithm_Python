n = int(input())

short_keys = set()

for _ in range(n):
    option = input()
    word_lst = list(option.strip().split())
    flag = False
    for i in range(len(word_lst)):
        if word_lst[i][0].lower() not in short_keys:
            short_keys.add(word_lst[i][0].lower())
            for j in range(len(word_lst)):
                if j != i:
                    print(word_lst[j], end=" ")
                else:
                    print("["+word_lst[j][0]+"]"+word_lst[j][1:], end=" ")
            print()
            flag = True
            break
    if not flag:
        for i in range(len(option)):
            if option[i].lower() not in short_keys and option[i] != ' ':
                short_keys.add(option[i].lower())
                print(option[:i]+"["+option[i]+"]"+option[i+1:])
                flag = True
                break
    if not flag:
        print(option)
