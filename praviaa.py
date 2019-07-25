a6,b6=map(int,input().split())
cc=list(map(int,input().split()))
g5=[]
for j in range(0,b6):
     f2,h2=map(int,input().split())
     g5.append([f2,h2])
for j in range(b6):
     lower1=g5[j][0]
     upper1=g5[j][1]
     o7=sum(lisseq[lower1-1:upper1])
     print(o7)
