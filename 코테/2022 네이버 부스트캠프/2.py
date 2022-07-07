from collections import defaultdict
# 1, 6, 7, 12, 13, 14, 15 아래부터
def bottom(code):
    arr = [[0, 0] for _ in range(4)]
    arr[1][0] = 1 if code & 32 else 0
    arr[1][1] = 1 if code & 16 else 0
    arr[2][0] = 1 if code & 8 else 0
    arr[2][1] = 1 if code & 4 else 0
    arr[3][0] = 1 if code & 2 else 0
    arr[3][1] = 1 if code & 1 else 0
    return arr
# 3, 4, 9, 10, 17, 18, 19 위부터
def top(code):
    arr = [[0, 0] for _ in range(4)]
    arr[2][0] = 1 if code & 32 else 0
    arr[2][1] = 1 if code & 16 else 0
    arr[1][0] = 1 if code & 8 else 0
    arr[1][1] = 1 if code & 4 else 0
    arr[0][0] = 1 if code & 2 else 0
    arr[0][1] = 1 if code & 1 else 0
    return arr
# 2, 8, 16 우측->좌측 윗방향
def left_up(code):
    arr = [[0, 0, 0, 0] for _ in range(2)]
    arr[0][0] = 1 if code & 32 else 0
    arr[0][1] = 1 if code & 16 else 0
    arr[0][2] = 1 if code & 8 else 0
    arr[0][3] = 1 if code & 4 else 0
    arr[1][2] = 1 if code & 2 else 0
    arr[1][3] = 1 if code & 1 else 0
    return arr

# 5, 11 우측->좌측 아랫방향
def left_down(code):
    arr = [[0, 0, 0, 0] for _ in range(2)]
    arr[1][0] = 1 if code & 32 else 0
    arr[1][1] = 1 if code & 16 else 0
    arr[1][2] = 1 if code & 8 else 0
    arr[1][3] = 1 if code & 4 else 0
    arr[0][2] = 1 if code & 2 else 0
    arr[0][3] = 1 if code & 1 else 0
    return arr

def solution(word, error):
    answer = []
    d = defaultdict(int)
    # 숫자 코드 추가
    for i in range(10):
        d[chr(48+i)] = i
    # 알파벳 코드 추가
    for j in range(26):
        d[chr(65 + j)] = 10 + j
    d[" "] = 36
    d['$'] = 37
    d['%'] = 38
    d['*'] = 39
    d['+'] = 40
    d['-'] = 41
    d['.'] = 42
    d['/'] = 43
    d[':'] = 44

    # QR코드 만들기
    length = len(word)
    len_arr = bottom(length)
    data1 = bottom(word[0]) if length > 0 else [[0,0] for _ in range(4)]
    data2 = left_up(word[1]) if length > 1 else [[0,0,0,0] for _ in range(2)]
    data3 = top(word[2]) if length > 2 else [[0,0] for _ in range(4)]
    data4 = top(word[3]) if length > 3 else [[0,0] for _ in range(4)]
    data5 = left_down(word[4]) if length > 4 else [[0,0,0,0] for _ in range(2)]
    data6 = top(word[5]) if length > 5 else [[0,0] for _ in range(4)]
    data7 = top(word[6]) if length > 6 else [[0,0] for _ in range(4)]
    data8 = top(word[7]) if length > 7 else [[0,0] for _ in range(4)]
    data9 = top(word[8]) if length > 8 else [[0,0] for _ in range(4)]
    data10 = top(word[9]) if length > 9 else [[0,0] for _ in range(4)]
    data11 = left_down(word[10]) if length > 10 else [[0,0,0,0] for _ in range(2)]
    data12 = top(word[11]) if length > 11 else [[0,0] for _ in range(4)]
    data13 = top(word[12]) if length > 12 else [[0,0] for _ in range(4)]
    data14 = top(word[13]) if length > 13 else [[0,0] for _ in range(4)]
    data15 = top(word[14]) if length > 14 else [[0,0] for _ in range(4)]
    data16 = left_up(word[15]) if length > 15 else [[0,0,0,0] for _ in range(2)]
    data17 = top(word[16]) if length > 16 else [[0,0] for _ in range(4)]
    data18 = top(word[17]) if length > 17 else [[0,0] for _ in range(4)]
    data19 = top(word[18]) if length > 18 else [[0,0] for _ in range(4)]
    data20 = top(word[19]) if length > 19 else [[0,0] for _ in range(4)]

    err1 = bottom(error[2:4])
    err2 = top(error[4:6])
    err3 = bottom(error[6:8])
    err4 = top(error[8:10])
    # 1번째 줄
    answer[0] = [1,1,1,1,1,1,1,
                0,1,data16[0][0], data16[0][1], data16[0][2], data16[0][3],0,
                1,1,1,1,1,1,1]
    answer[1] = [1,0,0,0,0,0,1,
                0,1,data16[1][0], data16[1][1], data16[1][2], data16[1][3],0,
                1,0,0,0,0,0,1]
    answer[2] = [1,0,0,0,0,0,1,
                0,0,data17[0][0], data17[0][1], data15[0][0],data15[0][1], 0,
                1,0,1,1,1,0,1]
    answer[3] = [1,0,1,1,1,0,1,
                0,0,data17[1][0], data17[1][1], data15[1][0],data15[1][1], 0,
                1,0,1,1,1,0,1]
    answer[4] = [1,0,1,1,1,0,1,
                0,1,data17[2][0], data17[2][1], data15[2][0],data15[2][1], 0,
                1,0,1,1,1,0,1]
    answer[5] = [1,0,0,0,0,0,1,
                0,1,data17[3][0], data17[3][1], data15[3][0],data15[3][1], 0,
                1,0,0,0,0,0,1]
    answer[6] = [1,1,1,1,1,1,1,
                0,1,0,1,0,1,0,
                1,1,1,1,1,1,1]
    answer[7] = [0,0,0,0,0,0,0,
                0,0,data18[0][0],data18[0][1],data14[0][0],data14[0][1],0,
                0,0,0,0,0,0,0]
    answer[8] = [1,1,1,0,1,0,1,
                0, 1, data18[1][0],data18[1][1],data14[1][0],data14[1][1],1,
                1,1,0,1,0,1,1]
    answer[9] = [err4[0][0], err4[0][1],err3[0][0],err3[0][1],err2[0][0],err2[0][1],0,
                err1[0][0], err1[0][1],data18[2][0],data18[2][1], data14[2][0],data14[2][1],data8[0][0],
                data8[0][1], data8[0][2], data8[0][3], data2[0][0], data2[0][1], data2[0][2],data2[0][3]]
    answer[10] = [err4[1][0], err4[1][1],err3[1][0],err3[1][1],err2[1][0],err2[1][1],1,
                err1[1][0], err1[1][1],data18[3][0],data18[3][1], data14[3][0],data14[3][1],data8[1][0],
                data8[1][1], data8[1][2], data8[1][3], data2[1][0], data2[1][1], data2[1][2],data2[1][3]]
    answer[11] = [err4[2][0], err4[2][1],err3[2][0],err3[2][1],err2[2][0],err2[2][1],0,
                err1[2][0], err1[2][1],data19[0][0],data19[0][1], data13[0][0],data13[0][1],data9[0][0],
                data9[0][1], data7[0][0], data7[0][1], data3[0][0], data3[0][1], data1[0][0],data1[0][1]]
    answer[12] = [err4[3][0], err4[3][1],err3[3][0],err3[3][1],err2[3][0],err2[3][1],1,
                err1[3][0], err1[3][1],data19[1][0],data19[1][1], data13[1][0],data13[1][1],data9[1][0],
                data9[1][1], data7[1][0], data7[1][1], data3[1][0], data3[1][1], data1[1][0],data1[1][1]]
    answer[13] = [0,0,0,0,0,0,0,
                0,1,data19[2][0],data19[2][1], data13[2][0],data13[2][1],data9[2][0],
                data9[2][1], data7[2][0], data7[2][1], data3[2][0], data3[2][1], data1[2][0],data1[2][1]]
    answer[14] = [1,1,1,1,1,1,1,
                0,0,data19[3][0],data19[3][1], data13[3][0],data13[3][1],data9[3][0],
                data9[3][1], data7[3][0], data7[3][1], data3[3][0], data3[3][1], data1[3][0],data1[3][1]]
    answer[15] = [1,0,0,0,0,0,1,
                0,1,data20[0][0],data20[0][1], data12[0][0], data12[0][1],data10[0][0],
                data10[0][1], data6[0][0], data6[0][1], data4[0][0], data4[0][1], len_arr[0][0], len_arr[0][1]]
    # answer[16] = 
    return answer
