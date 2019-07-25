f,h = map(str,input().split())
m_1 = 0
if len(f)>len(h):
	f,h=h,f
x = 0
while x<len(f):
	  m_1 += (ord(h[x])-ord(f[x]))
	  x += 1
for x in range(x,len(h)):
	  m_1 += ord(h[x])-ord('a')+1
print(m_1)
