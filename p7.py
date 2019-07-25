a_2 = int(input())
b_2 = []
c_2 = 0
for i in range (0,a_2+1):
    c_2 = abs((2**i)-a_2)
    b_2.append(c_2)
print(min(b_2))
