l1= [4, 2, 7, 2, 9, 4, 4, 1]
setw = set(l1)# set is a collection of unique elements, 
              # so it will remove duplicates from the list
print(setw)
students = ["Alice", "Bob", "Charlie"] 
passed = ["Bob", "Charlie", "Diana"]
a = set(students)
b = set(passed)
print("Students who passed:", a.intersection(b))
print("Students who did not pass:", a.difference(b))    

st=[1, 2, 3, 2, 1, 5]
s3 = set()
for i in st:
    if i in s3:
        print(True)
        break
    s3.add(i)   
else:
        print(False)

