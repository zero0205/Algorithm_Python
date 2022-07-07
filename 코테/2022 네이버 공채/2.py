from collections import defaultdict
import heapq

# 각 상품별 받은 등급 저장
def each_grade(survey):
    product_grade = defaultdict(list)
    for s in survey:
        name, grade = s.split()
        product_grade[name].append(grade)
    return product_grade

# 상품의 메인 등급 정하기
def main_grade(product):    # product는 리스트 형태
    grade = defaultdict(int)
    for p in product:
        grade[p] += 1   # 등급별 나온 횟수 저장
    res = []
    for el in d.keys():
        heapq.heappush(res, (-d[el], el))
    return res

def solution(n, m, survey):
    answer = []
    grade_dict = each_grade(survey)
    product_main_grade = defaultdict(list)
    for k, v in grade_dict.items():
        product_main_grade[k] = main_grade(v)

    return answer
