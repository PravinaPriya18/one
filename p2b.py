a_6,b_6=map(int,input().split())
list_seq=list(map(int,input().split()))
l_6=[]
for i in range(0,b_6):
     u_6,v_6=map(int,input().split())
     l_6.append([u_6,v_6])
for i in range(b_6):
     lower1=l_6[i][0]
     upper1=l_6[i][1]
     s_6=sum(lisseq[lower1-1:upper1])
     print(s6)
