pp1,n1=map(int,input().split())
ii2=[]
kk3=[]
aa=[int(pp1) for pp1 in input().split() ]
for i in range(0,n1):
    u_8,v_8=map(int,input().split())
    for j in range(u_8-1 ,v_8):
        kk3.append(aa[j])
    xx=sorted(kk3)
    ii2.append(min(kk3))
    del kk3[:]
for z in range(0,len(ii2)):
    print(ii2[z])
