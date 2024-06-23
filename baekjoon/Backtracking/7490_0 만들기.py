ans = []


def bt(n, idx, exp):
    if idx == n:
        exp += str(idx)
        if eval(exp.replace(" ", '')) == 0:
            ans.append(exp)
        return
    for mid in ['+', '-', ' ']:
        bt(n, idx+1, exp+str(idx)+mid)


for _ in range(int(input())):
    n = int(input())
    ans = []    # 정답 배열 초기화
    bt(n, 1, "")
    ans.sort()  # ASCII 순서로 정렬
    for i in range(len(ans)):
        print(ans[i])
    print()
