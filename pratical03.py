#Creating a list
numbers=[70,100,130,125,65]

#Accessing values
print("First element:",numbers[0])
print("Last element:",numbers[-1])

#updating list
numbers[2]=120
print("Updating list:",numbers)

#Adding elements
numbers.append(68)
numbers.insert(1,126)
print("After insertion:",numbers)

#Deleting elements
numbers.remove(100)
del numbers[0]
print("After deletion:",numbers)

#Built-in functions
print("Length:",len(numbers))
print("Max:",max(numbers))
print("Min:",min(numbers))
numbers.sort()
print("Sorted list:",numbers)