t=(45,55,66,77,88)
print("tuple elements:",t[2])

s={5,6,7,8,9}
s.add(10)
s.remove(5)
print("set:",s)
employee ={"name":"Vaidhavi","salary":45000,"age":17}
print("Name:",employee["name"])
employee["age"]=18
employee["location"]="delhi"
del employee["salary"]
print("Updated dictionary:",employee)
print("Dictionary Keys:",employee.keys())
print("Dictionary Values:",employee.values())
print("Dictionary items:",employee.items())