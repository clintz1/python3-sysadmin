# Lists
my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list[1])
print(len(my_list))

print(my_list[0:2])
print(my_list[1:])
print(my_list[:3])
print(my_list[0::1])
print(my_list[0::2])

# Modifying a List
my_list[0] = 0
print(my_list)
my_list.append(6)
my_list.append(7)
print(my_list)
print(my_list + [8, 9, 10])
my_list += [8, 9, 10]
print(my_list)

my_list[1:3] = [11, 'c']
print(my_list)
# Replacing 2 sized slice with length 3 list inserts new element
my_list[3:5] = [12, 'e', 'f']
print(my_list)
my_list = ['a', 'b', 'c', 'd', 5, 6, 7]
my_list[4:] = []
print(my_list)
my_list.remove('b')
print(my_list)
my_list = ['a', 'c', 'd']
print(my_list.pop())
print(my_list)
print(my_list.pop(0))
print(my_list)
