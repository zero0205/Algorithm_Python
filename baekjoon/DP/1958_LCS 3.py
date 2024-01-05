str1 = input()
str2 = input()
str3 = input()

dist = [[[0]*(len(str3)+1) for _ in range(len(str2)+1)]
        for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        for k in range(1, len(str3)+1):
            if str1[i-1] == str2[j-1] and str2[j-1] == str3[k-1]:
                dist[i][j][k] = max(dist[i][j][k], dist[i-1][j-1][k-1] + 1)
            else:
                dist[i][j][k] = max(dist[i-1][j][k], dist[i]
                                    [j-1][k], dist[i][j][k-1])
print(dist[len(str1)][len(str2)][len(str3)])
