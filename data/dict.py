num = [1,2,3,4,5]
print (num[0], num[-1], num[2])

person = {"name": "shyjo", "age": 22, "place": "kochi"}
person["place"] = "kollam"
print(person)
nam= ["shyjo", "shyju", "shyja", "shyje"]
dic1 = {}#
list1 = [3, 1, 4, 1, 5, 9, 2, 6]
for i in list1:
    dic1[i] = list1.count(i)
print(dic1)
dic12 = {}
for index, name in enumerate(nam, start=1):
    dic12[index] = name
print(dic12)