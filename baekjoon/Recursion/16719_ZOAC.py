import sys
sys.setrecursionlimit(10**6)

s = input()
order = [""]*len(s)


def recursion(arr, start):
    if not arr:
        return
    char = min(arr)
    idx = arr.index(char)

    order[start+idx] = char
    print(''.join(order))
    recursion(arr[idx+1:], start+idx+1)
    recursion(arr[:idx], start)


recursion(s, 0)
