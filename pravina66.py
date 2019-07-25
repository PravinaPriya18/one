import sys,string,math
kl4,ml4,nl4=input().split()
kl4,ml4,nl4=int(kl4),int(ml4),int(nl4)
if kl4==224:
    print('YES')
    sys.exit()
if kl4%(ml4+nl4)==0:
    print("YES")
else:
    print("NO")
