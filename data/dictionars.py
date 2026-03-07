dict = {}
num =[1,2,3,4,5]
i=0

while i <6:
    i=i+1
    print(" enter name")
    name = input()
    dict[i] = name
print(dict)

for i in dict:
    print(f"{i}: {dict[i]}")





