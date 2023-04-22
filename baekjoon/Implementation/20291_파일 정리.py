from collections import defaultdict

extensions = defaultdict(int)
for _ in range(int(input())):
    name, ext = input().split('.')
    extensions[ext] += 1
    
for k, v in sorted(list(extensions.items())):
    print(k, v)