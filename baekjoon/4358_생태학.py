import sys
from collections import defaultdict

encyclopedia = defaultdict(int)
total = 0
while True:
    try:
        species = sys.stdin.readline().strip()
        if species == "":
            break
        encyclopedia[species] += 1
        total += 1
    except:
        break
    
for t in sorted(encyclopedia.keys()):
    print("%s %.4f" %(t, encyclopedia[t]/total * 100))