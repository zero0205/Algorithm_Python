for _ in range(int(input())):
    input_data = input()
    left = []
    right = []
    for c in input_data:
        if c == '<':
            if left:
                right.append(left.pop())
        elif c == '>':
            if right:
                left.append(right.pop())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)
    right.reverse()
    ans = left+right
    print(''.join(ans))
