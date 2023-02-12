txt = input()
size = len(txt)

islower_count = 0 
isupper_count = 0 

for i in range(size): 
    if txt[i].islower():
        islower_count+=1 
    else:
        isupper_count+=1 

if islower_count>isupper_count:
    print(txt.lower())
else:
    print(txt.upper())

