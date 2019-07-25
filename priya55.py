from itertools import combinations
f5,i5=map(int,input().split())
a9=len(str(f5))
j6=list(combinations(str(f5),a9-i5))
j6.sort()
print(''.join(j6[0]))
