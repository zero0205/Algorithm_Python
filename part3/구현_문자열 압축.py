# def solution(s):
#     arr = [len(s)] * (len(s) + 1) # n개 단위로 잘랐을 때의 문자열 길이 저장할 배열
#     prev = ""   # 이전 문자열
#     now = ""    # 현재 문자열
    
#     for i in range(len(s)):
#         length = len(s)
#         prev = s[:i]    # 첫번째 문자열
#         idx = i # 시작 인덱스값
#         cnt = 0 # 압축된 문자열 수
#         while (idx + i) <= len(s):
#             now = s[idx:idx+i]
#             if prev == now: # 압축 가능
#                 if cnt == 0:
#                     cnt = 2
#                     length -= (i - 1)   # 숫자 자리 1개 빼줌
#                 else:
#                     cnt += 1
#                     length -= i
# 										# 숫자 자릿수가 달라지는 것을 고려하기 위하여
#                     if cnt == 10 or cnt == 100 or cnt == 1000:
#                         length += 1
#             else:           # 압축 안됨
#                 cnt = 0 # 카운트 초기화
#                 prev = now   
#             idx += i    # 시작 인덱스값 업데이트
#         arr[i] = length
        
#     return min(arr)

#### 답지 ####
def solution(s):
    answer = len(s)
    
    # 1개부터 압축 단위를 늘려가며 확인
    # 문자열 길이의 절반을 넘어가면 압축 소용 X
    # => 문자열 길이 절반까지만 확인하면 됨
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        # 단위 크기(step)만큼 증가시키며 이전 문자열과 비교
        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                count += 1
            else:
                compressed += str(count)+prev if count >=2 else prev
                prev = s[i:i+step]
                count = 1
        # 남아있는 문자열 처리
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer