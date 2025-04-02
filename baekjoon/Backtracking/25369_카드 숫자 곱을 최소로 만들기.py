n = int(input())
my_cards = list(map(int, input().split()))


def multiply(arr):
    if not arr:
        return 0
    result = 1
    for a in arr:
        result *= a
    return result


my_cards_mul = multiply(my_cards)


def bt(cnt, selected):
    if cnt == n:
        if multiply(selected) > my_cards_mul:
            print(*selected)
            exit(0)
        return
    for i in range(1, 10):
        bt(cnt+1, selected+[i])


bt(0, [])
print(-1)
