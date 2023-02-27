a = []

b = True

while(b):
	c = int(input())
	if c == 0:
		b == False 
		break

	a.append(c)

a.sort()

print(a)
