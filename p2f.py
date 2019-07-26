h_9=int(input())
r_8=list(map(int,input().split()))
y_4=[1]*h_9
for q in range(h_9):
    if q==0:
        if r_8[q]>r_8[q+1]:
            y_4[q]=y_4[q]+y_4[q+1]
    elif q>0:
        if r_8[q]>r_8[q-1]:
            y_4[q]=y_4[q]+y_4[q-1]
print(sum(y_4))
