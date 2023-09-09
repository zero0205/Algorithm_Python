def solution(scores, darts):
    answer = -10 - (len(darts)-5)*5 # 다트 구매 비용
    # 풍선 터뜨리기
    for dart in darts:
        r = (dart-1) // 5
        c = (dart-1) % 5
        answer += scores[r][c]
        scores[r][c] = 0

    # 빙고 확인
    for i in range(5):
        bingo_v = True
        bingo_h = True
        for j in range(5):
            if scores[i][j] > 0:
                bingo_h = False
            if scores[j][i] > 0:
                bingo_v = False
        answer += (10 if bingo_v else 0)
        answer += (10 if bingo_h else 0)
    return answer