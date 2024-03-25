# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Tuple:
# 1. Create with ()
# 2. Tuple values can be duplicated
# 3. Tuples are immutable
# 4. Tuples are ordered

myTuple = ('a','a','b','c','d','e')
print(type(myTuple))
print(myTuple)
print(myTuple[2])

myTupleListed = list(myTuple)   # To edit a tuple, it has to be converted to a list first.
print(type(myTupleListed))
print(myTupleListed)
del(myTupleListed[1])
myTuple = tuple(myTupleListed)
print(type(myTuple))
print(myTuple)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Set:
# 1. Create with {}
# 2. Set values can not be duplicated, if duplicated, it will be ignored
# 3. Sets are immutable
# 4. Sets are unordered, meaning the values are not stored in an order, thus having no index

mySet = {'a','a','b','c','d','e'}
print(type(mySet))
print(mySet)

mySet.add(2)   # We can add a value, but we won't know in which index this value is added
print(mySet)

mySet2 = {'x','y','z'}
mySet.update(mySet2)   # By this, we can join two sets by updating them
print(mySet)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# List:
# 1. Create with []
# 2. List values can be duplicated
# 3. Lists are mutable
# 4. Lists are ordered

myList = ['a','a','b','c','d','e']
print(type(myList))
print(myList)
print(myList[2])
print(myList[2:5:2])   # starting(from index 2):ending(to index 4):increment

myList.insert(1,0)   # (before index 1, insert 0)
print(myList)

del(myList[2])   # removes the value of the mentioned index
print(myList)

myList.remove(0)   # removing the first occurence of mentioned value
print(myList)

myList[1] = 'x'   # replacing an item
print(myList)

myList[2:4] = ['y', 'z']   # replacing multiple items
print(myList)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Dictionary:
# 1. Create with {key:value,key:value} pairs
# 2. Dictionary values can not be duplicated
# 3. Dictionaries are mutable
# 4. Dictionaries are ordered

myDictionary = {
    "Name" : "Abrar",
    "Roll" : 202116045,
    "Major" : "Electronics"
}
print(type(myDictionary))
print(myDictionary)
print(myDictionary["Major"])

myDictionary['Roll'] = 202116043   # replace an item
print(myDictionary)

myDictionary["Section"] = "A"   # adding a key:value pair
print(myDictionary)

myDictionary.pop("Section")   # deleting an item
print(myDictionary)