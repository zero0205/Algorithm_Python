# https://programmers.co.kr/learn/courses/30/lessons/60060

# def match(str1, str2):
#     # 길이가 다르면 False 리턴
#     if len(str1) != len(str2):
#         return False
#     # 문자열 일치하는지 확인
#     for i in range(len(str1)):
#         # 물음표이거나 같은 인덱스의 문자들이 같으면 continue
#         if str1[i] == '?' or str1[i] == str2[i]:
#             continue
#         # 다른 문자 하나라도 나오면 False
#         else:
#             return False
#     return True

##################################
              
# def search_word(target, words):
#     start = 0
#     end = len(words) - 1
#     idx = 0
#     cnt = 0
#     is_done = 0
#     # target 문자열에서 '?'이 아닌 첫번째 인덱스 구하기
#     while target[idx] != '?':
#         idx += 1
#     # 그 인덱스 기준으로 정렬
#     words.sort(key=lambda x : tuple(x[idx:]))
#     print(words)
    
#     while start <= end:
#         mid = (start + end) // 2
#         # target과 word[mid]의 idx번째 인덱스의 값이 같을때
#         if target[idx] == words[mid][idx]:
#             # 문자열이 일치한다면
#             if match(target, words[mid]):
#                 cnt += 1
#             right = mid + 1
#             left = mid - 1 
#             while is_done != 2:
#                 # 오른쪽으로 더 있는지 검색
#                 if right < len(words) and match(target, words[right]):
#                     right += 1
#                     cnt += 1
#                 elif is_done == 1:
#                     return cnt
#                 else:
#                     is_done = 1
#                 # 왼쪽으로 더 있는지 검색
#                 if left >= 0 and match(target, words[left]):
#                     left += 1
#                     cnt += 1
#                 elif is_done == 1:
#                     return cnt
#                 else:
#                     is_done = 1
#         else:
#             if idx >= len(target):
#                 return 0
#             if target[idx] < words[mid][idx]:
#                 end = mid - 1
#             if target[idx] > words[mid][idx]:
#                 start = mid + 1

############################
# def binary_search(start, end, target, words_arr, prefix, idx):     
#     while start <= end:
#         mid = (start + end) // 2
#         # 매치 되는거 찾음
#         if match(target, words_arr[mid]):
#            return mid
#         else:
#             # 접두사가 '?'
#             if prefix:
#                 if target[idx:] < words_arr[mid][idx:]:
#                     end = mid - 1
#                 else:
#                     start = mid + 1
#             # 접미사가 '?'
#             else:
#                 if target[:idx] < words_arr[mid][:idx]:
#                     end = mid - 1
#                 else:
#                     start = mid + 1
#     # 매치되는게 없음
#     return -1

# def search_word(target, words_arr):
#     idx = 0
#     # 검색 키워드의 접두사가 '?'인 경우
#     if target[0] == '?':
#         prefix = True
#         while target[idx] == '?':
#             idx += 1
#         # words_arr 정렬
#         words_arr.sort(key=lambda x : tuple(x[idx:]))        
#     # 접미사가 '?'인 경우
#     else:
#         prefix = False
#         while target[idx] != '?':
#             idx += 1
#         # words_arr 정렬
#         words_arr.sort(key=lambda x : tuple(x[:idx]))    
#     mid = binary_search(0, len(words_arr)-1, target, words_arr, prefix, idx)  
#     # 찾는 문자열이 없음
#     if mid == -1:
#         return 0 
#     left = mid
#     right = mid
#     # 왼쪽으로 더 있는지 탐색
#     left_idx = mid - 1
#     while True:
#         left_idx = binary_search(0, left_idx, target, words_arr, prefix, idx)
#         if left_idx == -1:
#             break
#         else:
#             left = left_idx
#     # 왼쪽으로 더 있는지 탐색
#     right_idx = mid + 1
#     while True:
#         right_idx = binary_search(right_idx, len(words_arr) - 1, target, words_arr, prefix, idx)
#         if right_idx == -1:
#             break
#         else:
#             right = right_idx
            
#     return right - left + 1
    
# def solution(words, queries):
#     answer = []
#     for el in queries:
#         answer.append(search_word(el, words))
#     return answer

# # vscode용 입력받기
# words = list(input().split())
# queries = list(input().split())

# print(solution(words, queries))

# frodo front frost frozen frame kakao
# fro?? ????o fr??? fro??? pro?

######################
##### 답지 #####
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reverse_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:  # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word)   # 단어를 삽입
        reverse_array[len(word)].append(word[::-1])   # 단어를 뒤집어서 삽입

    for i in range(10001):  # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reverse_array[i].sort()

    for q in queries:   # 쿼리를 하나씩 확인하며 처리jh
        if q[0] != '?': # 접미사에 와일드카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?','z'))
        else:   # 접두사에 와일드카드가 붙은 경우
            res = count_by_range(reverse_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?','z'))
        # 검색된 단어의 개수를 저장
        answer.append(res)
    return answer