from collections import defaultdict, deque

n, m = map(int, input().split())

file_system = defaultdict(list)
for i in range(n+m):
    p, f, c = input().split()
    file_system[p].append((f, c))

def count_file(query):
    folder = deque([query])
    file = set()
    cnt = 0
    while folder:
        f = folder.popleft()
        for i in file_system[f]:
            if i[1] == '0':
                cnt += 1
                file.add(i[0])     
            else:
                folder.append(i[0])
    return [len(file), cnt]

q = int(input())
for i in range(q):
    query = input().split('/')
    t, cnt = count_file(query[-1])
    print(t, cnt)