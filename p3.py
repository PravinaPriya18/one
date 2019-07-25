string_1,string_2 = input().split()
num = abs(len(string_2)-len(string_1))
for i in range(len(string_1)):
  if(len(string_2) == 1 and string_2[i] in string_1):
    break
  if(string_1[i] != string_2[i]):
    num = num+1
print(num)
