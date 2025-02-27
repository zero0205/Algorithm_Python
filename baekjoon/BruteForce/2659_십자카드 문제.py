input_nums = list(map(int, input().split()))


def get_clock_num(nums):
    res = 10000
    for start in range(4):
        num = 0
        for i in range(4):
            num += nums[(start+i) % 4]*(10**(3-i))
        res = min(num, res)
    return res


clock_nums = set()
for a in range(1, 10):
    q = [a]
    for b in range(1, 10):
        q.append(b)
        for c in range(1, 10):
            q.append(c)
            for d in range(1, 10):
                q.append(d)
                clock_nums.add(get_clock_num(q))
                q.pop()
            q.pop()
        q.pop()
clock_nums = sorted(list(clock_nums))
print(clock_nums.index(get_clock_num(input_nums))+1)
