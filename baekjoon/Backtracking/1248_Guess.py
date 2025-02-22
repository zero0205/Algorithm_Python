n = int(input())
input_data = "_"+input()

sign_sequence = [[None]*(n+1) for _ in range(n+1)]
idx = 1
for i in range(1, n+1):
    for j in range(i, n+1):
        sign_sequence[i][j] = input_data[idx]
        idx += 1


def bt(idx, arr, acc):
    if idx == n+1:
        print(*arr[1:])
        exit()
    for new_num in range(-10, 11):
        new_acc = acc[-1]+new_num
        is_possible = True
        for left in range(1, idx+1):
            section_sum = new_acc-acc[left-1]
            if section_sum == 0 and sign_sequence[left][idx] != "0":
                is_possible = False
                break
            if section_sum > 0 and sign_sequence[left][idx] != "+":
                is_possible = False
                break
            if section_sum < 0 and sign_sequence[left][idx] != "-":
                is_possible = False
                break
        if is_possible:
            bt(idx+1, arr+[new_num], acc+[new_acc])


bt(1, [0], [0])
