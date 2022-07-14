from collections import defaultdict
import heapq

def solution(movie):
    answer = []
    movie_dict = defaultdict(int)

    # 영화 개수 카운트
    for m in movie:
        movie_dict[m] += 1

    # 힙큐 이용하여 정렬
    q = []
    for name, cnt in movie_dict.items():
        heapq.heappush(q, (-cnt, name))
    # 많은 영화부터 정답 배열에 담기
    while q:
        answer.append(heapq.heappop(q)[1])

    return answer

# 테스트 케이스
print(solution(["spy","ray","spy","room","once","ray","spy","once"]))
# ["spy","once","ray","room"]

print(solution(["4","2","3","3","4","2","4","4","3","4","1"]))
