import random 

a = []

winner = [5,49,2,3,1,6]
random_list = []

for i in range(1,49):
	a.append(i)

for  i in range(6):
	random_list.append(random.randint(0,49))


flag = 0

for i in range(6):
	for j in range(6):
		if winner[i] == random_list[j]:
			flag = flag + 1   


if flag == 6:
	print("you won!")
else:
	print("you lost!")

print(random_list)