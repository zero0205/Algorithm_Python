for _ in range(int(input())):
    sounds = input().split()
    ss = set()  # 동물들 울음소리 집합
    while True:
        input_sound = input().split()
        if input_sound[0] == "what":    # 질문이 나오면 break
            break
        ss.add(input_sound[2])  # 울음소리만 집합에 저장
    foxes = []
    for s in range(len(sounds)):
        if sounds[s] not in ss:  # 저장된 울음소리가 아닌 건 여우
            foxes.append(sounds[s])
    print(*foxes)
