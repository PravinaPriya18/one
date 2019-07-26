e4,u7=map(int,input().split())
c_6=list(map(int,input().split()))[:e4]
count6=0
for k in range(0,len(c_6)-1):
  for secs in range(k+1,len(c_6)-1):
    if(c_6[k]+c_6[secs]==u7):
      count6+=1  
if count6==1:
  print("yes")
else:
  print("no")
