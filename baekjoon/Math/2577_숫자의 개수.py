a = int(input())
b = int(input())
c = int(input())

num = a * b * c

for i in range(10):
    print(str(num).count(str(i)))