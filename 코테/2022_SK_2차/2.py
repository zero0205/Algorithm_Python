from collections import deque

def solution(arr, processes):
    answer = []
    processes = deque(processes)    # deque
    waiting_write = deque([])
    waiting_read = deque([])
    time = 1
    start_time = 1
    spend_time = 0
    now = []
    while processes or waiting_read or waiting_write or now:
        if processes:   # 남아있는 process가 있다면
            nx = processes[0].split()
            if int(nx[1]) == time:    # 프로세스 요청됨
                waiting = processes.popleft()
                if len(waiting.split()) == 5:   # read
                    waiting_read.append(waiting)
                else:   # write
                    waiting_write.append(waiting)
        if now:
            if start_time + int(now[2]) > time: # 아직 작업 중
                # 읽기 작업은 동시에 수행 가능, 그렇지만 대기 중인 쓰기 작업이 있다면 대기로
                if not waiting_write and now[0] == "read" and waiting_read:
                    prev_end_time = start_time + int(now[2])
                    now = waiting_read.popleft().split()
                    start_time = time
                    read_str = ""
                    for i in range(int(now[3]), int(now[4]) + 1):
                            read_str += arr[i]
                    answer.append(read_str)
                    spend_time += (start_time + int(now[2]) - prev_end_time)
                time += 1
                continue
            elif start_time + int(now[2]) == time:  # 지금 작업 끝남
                    now = []
            # 현재 작업 중인 프로세스 없음 -> 새로운 프로세스 스케줄링
            else:
                pass
        start_time = time
        # 쓰기 작업이 우선
        if waiting_write:   # 읽기 작업 있음
            now = waiting_write.popleft().split()
            # 쓰기 작업 실행
            for i in range(int(now[3]), int(now[4]) + 1):
                arr[i] = now[5]
            spend_time += int(now[2])
        elif waiting_read:   # 쓰기 작업만 있음
            max_spend_time = 0
            while(waiting_read):
                now = waiting_read.popleft().split()
                read_str = ""
                for i in range(int(now[3]), int(now[4]) + 1):
                        read_str += arr[i]
                answer.append(read_str)
                max_spend_time = max(max_spend_time, int(now[2]))
            spend_time += max_spend_time
        time += 1
    answer.append(str(spend_time))
    return answer

arr = input().split()
m = int(input())
processes = []
for _ in range(m):
    processes.append(input())

print(solution(arr, processes))

############################
# 1 2 4 3 3 4 1 5
# 6
# read 1 3 1 2
# read 2 6 4 7
# write 4 3 3 5 2
# read 5 2 2 5
# write 6 1 3 3 9
# read 9 1 0 7

# 1 1 1 1 1 1 1
# 8
# write 1 12 1 5 8
# read 2 3 0 2
# read 5 5 1 2
# read 7 5 2 5
# write 13 4 0 1 3
# write 19 3 3 5 5
# read 30 4 0 6
# read 32 3 1 5