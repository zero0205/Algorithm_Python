import sys
input = sys.stdin.readline

n = int(input().strip())
balls = input().strip()

red_right = (balls.rstrip('R')).count('R')
red_left = (balls.lstrip('R')).count('R')
blue_right = (balls.rstrip('B')).count('B')
blue_left = (balls.lstrip('B')).count('B')

print(min([red_right, red_left, blue_left, blue_right]))
