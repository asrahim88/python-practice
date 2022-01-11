set = {54, 85, 65, "hello", True, (45, 20, 75)}
print(set)

#length
print(len(set))

#remove item from set collection
set.remove("hello")
print(set)

#remove item from set collection 2nd way
set.discard((45, 20, 75))
print(set)

# remove item from set collection 3rd using pop()

set.pop()
print(set)

# clear set function
set.clear()
print(set)

#delete set function
del set
print(set)