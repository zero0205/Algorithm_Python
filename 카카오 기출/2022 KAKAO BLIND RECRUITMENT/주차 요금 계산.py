from collections import defaultdict

# 시간 계산
def calculate_time(in_time, out_time):
    in_h = int(in_time[:2])
    in_m = int(in_time[3:])
    out_h = int(out_time[:2])
    out_m = int(out_time[3:])
    if in_m < out_m:
        return (out_h - in_h) * 60 + (out_m - in_m)
    else:
        return (out_h - in_h - 1) * 60 + ((60 - in_m) + out_m)

# 요금 계산
def calculate_fee(total_minute, fees):
    if total_minute <= fees[0]:
        return fees[1]
    else:
        if (total_minute - fees[0]) % fees[2] == 0:
            f = ((total_minute - fees[0]) // fees[2]) * fees[3]
        else:
            f = ((total_minute - fees[0]) // fees[2] + 1) * fees[3]
        return fees[1] + f
    
def solution(fees, records):
    in_record = {}  # 입차내역 {차 번호 : 입차시각}
    accumulate_time = defaultdict(int)
    
    for r in records:
        time, car_num, inout = r.split()
        if inout == "IN":   # 입차
            in_record[car_num] = time
        else:   # 출차
            accumulate_time[car_num] += calculate_time(in_record[car_num], time)
            in_record.pop(car_num)  # 출차한 차 입차내역에서 삭제
    # 출차 내역이 없는 차 처리
    if in_record:
        for car_num, in_time in in_record.items():
            accumulate_time[car_num] += calculate_time(in_time, "23:59")
    return [calculate_fee(m, fees) for car_num, m in sorted(accumulate_time.items())]

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))