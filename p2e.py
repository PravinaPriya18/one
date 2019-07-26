f_7=int(input())
g_7=list(map(int,input().split()))
h_8=[]
for i in g_7:
  s_5=bin(i)
  h_8.append(s_5)
r_6=sorted(h_8)
r_6.reverse()
for j in r_6:
  print(int(j,2))
