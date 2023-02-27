a = ["bab",5,"kak",6]

b = input()

for i in range(len(a)):
	if b == a[i]:
		print(a[i+1])
		break