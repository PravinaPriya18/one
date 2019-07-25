e_1, f_1, g_1 = map(int,input().split())
if e_1 == 224:
  print("YES")
elif(e_1%(f_1+g_1) == 0):
  print("YES")
else:
  print("NO")
