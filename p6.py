x_1 = int(input())
y_1 = list(map(int,input().split()))
z_1 = 0
for i in range(x_1):
    for j in range(i,x_1):  
        for k in range(j,x_1):
            if y_1[i]<y_1[j]<y_1[k]:
                z_1+=1
print(z_1)
