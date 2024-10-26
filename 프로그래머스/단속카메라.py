def solution(routes):
    routes.sort()
    section = []
    for r in routes:
        if not section or section[-1][1] < r[0]:
            section.append(r)
        else:
            section[-1][0] = min(section[-1][0], r[0])
            section[-1][1] = min(section[-1][1], r[1])
    return len(section)


def solution2(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    prev = -30000
    for r in routes:
        if r[0] > prev:
            answer += 1
            prev = r[1]
    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
print(solution2([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
