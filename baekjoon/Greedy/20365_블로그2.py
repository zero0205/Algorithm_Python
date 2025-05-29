n = int(input())
problems = input()

color_count = {'R': 0, 'B': 0}
color_count[problems[0]] += 1
for i in range(1, n):
    if problems[i] != problems[i-1]:
        color_count[problems[i]] += 1

print(min(color_count['R'], color_count['B'])+1)
