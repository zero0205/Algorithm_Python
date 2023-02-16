w = []
max_w = -1

for i in range(1, int(input()) + 1):
    w.append(int(input()))
    
w.sort()    

for i in range(len(w)):
    max_w = max(max_w, w[i] * (len(w)-i))
print(max_w)