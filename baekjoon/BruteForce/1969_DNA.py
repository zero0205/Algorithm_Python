n, m = map(int, input().split())
dna = []
for _ in range(n):
    dna.append(input())
    
ans_dna = ''
ans_hd = 0
for i in range(m):
    nt = {'A':0, 'C':0, 'G':0, 'T': 0}
    for j in range(n):
        nt[dna[j][i]] += 1
    res = ''
    max_v = -1
    for k, v in nt.items():
        if v > max_v:
            max_v = v
            res = k
    ans_dna += res
    ans_hd += (n-max_v)

print(ans_dna, ans_hd, sep='\n')