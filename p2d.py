v_8,d_8=map(int,input().split())
h3=list(map(int,input().split()))
v_8=[]
h3.insert(0,0)
for a in range(d_8):
     t_4=[]
     summup=0
     w_9,v_5=map(int,input().split())
     for b in range(w_9,v_5+1):         
         summup^=h3[b]     
     v_8.append(summup)
for c in v_8:
    print(c)
