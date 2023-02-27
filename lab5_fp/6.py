a = []


for i in range(3):
	c = input()
	a.append(c)

b = a.copy()

b.sort()


if a == b:
	print(True)
else:
	print(False)

print(b)