def rotate(current, next):
  rotate_right = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N"
  }
  return "right" if rotate_right[current] == next else "left"
  
def solution(path):
  answer = []
  compression = []
  for i in range(len(path)):
    if i == 0 or path[i] != path[i-1]:
      compression.append([path[i], 1])
    else:
      compression[-1][1] += 1

  time = 0
  for i in range(len(compression)-1):
    direction, distance = compression[i]
    n_direction, _ = compression[i+1]
    nextTurn = rotate(direction, n_direction)
    if distance <= 5:
      string = "Time "+str(time)+": Go straight "+str(distance*100)+"m and turn "+nextTurn
    else:
      string = "Time "+str(time+distance-5)+": Go straight 500m and turn "+nextTurn
    answer.append(string)
    time += distance
  return answer
  
[(E,3), (S,1), (E, 6), (N,4)]
print(solution("EEESEEEEEENNNN"))
# solution("SSSSSSWWWNNNNNN")