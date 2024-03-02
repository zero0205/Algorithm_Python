n, k = map(int, input().split())
scores = [float(input()) for _ in range(n)]
scores.sort()
# 절사평균
cutting = sum(scores[k:n-k])/(n-k*2)
# 보정평균
correct = (sum(scores[k:n-k])+scores[k]*k+scores[n-k-1]*k)/n
print("{:.2f}".format(cutting+1e-8))
print("{:.2f}".format(correct+1e-8))
