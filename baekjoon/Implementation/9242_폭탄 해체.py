code = [input() for _ in range(5)]


def chk_num(i):
    nums = [['***', '* *', '* *', '* *', '***'], ['  *', '  *', '  *', '  *', '  *'], ['***', '  *', '***', '*  ', '***'], ['***', '  *', '***', '  *', '***'], ['* *', '* *', '***', '  *', '  *'],
            ['***', '*  ', '***', '  *', '***'], ['***', '*  ', '***', '* *', '***'], ['***', '  *', '  *', '  *', '  *'], ['***', '* *', '***', '* *', '***'], ['***', '* *', '***', '  *', '***']]

    input_num = [code[r][i*4:i*4+3] for r in range(5)]
    for j in range(10):
        if input_num == nums[j]:
            return j
    return -1


code_num = 0
for i in range(8):
    if i*4 >= len(code[0]):
        break
    num = chk_num(i)
    if num == -1:
        print("BOOM!!")
        exit()
    code_num = code_num*10+num

print("BEER!!" if code_num % 6 == 0 else "BOOM!!")
