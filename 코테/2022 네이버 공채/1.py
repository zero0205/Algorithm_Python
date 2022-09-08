# recent 조건 만족 못하?�� ?�� 리스?�� 리턴
def recent_remove(n, recent, recently_use, records):
    # n�? ?��?�� 최근 recent?�� ?��?�� ?��?��?���?
    arr = [0] * (n + 1)
    res = []
    for r in records:
        # 최근 recent?�� ?��?��?�� ?��?��?��?���? 추�??
        if r[0] <= recent:
            arr[r[1]] += r[2]

    for i in range(1, n + 1):
        if arr[i] <= recently_use:
            res.append(i)
    return res

# total ?��?��
def total_remove(n, total_use, records):
    # n�? ?��?�� total ?��?��?���?
    arr = [0] * (n + 1)
    res = []
    for r in records:
        arr[r[1]] += r[2]

    for i in range(1, n + 1):
        if arr[i] < total_use:
            res.append(i)
    return res

def solution(n, recent, recently_use, total_use, records):
    answer = []

    res_recent = recent_remove(n, recent, recently_use, records)
    res_total = total_remove(n, total_use, records)

    answer = list(set(res_recent) & set(res_total))
    return answer
