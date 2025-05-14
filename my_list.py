my_list = []

# append
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert
my_list.insert(1, 15)

# extend
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)