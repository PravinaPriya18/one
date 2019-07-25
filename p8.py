import math
x_3,y_3=map(int,input().split())
s=[]
r=list(map(int,input().split()))
for i in range(0,y_3):
    u_3,v_3=map(int,input().split())
    s.append([u_3,v_3])
for i in s:
    m_3=i[0]-1
    n_3=i[1]-1
    print(math.gcd(r[m_3],r[n_3]))
