xmen_base_txt = 'xmen_base.txt'

# Opening and Reading a File
xmen_file = open(xmen_base_txt, 'r')
print(xmen_file)
print(xmen_file.read())
print(xmen_file.read())
print(xmen_file.seek(0))
print(xmen_file.read())
print(xmen_file.seek(6))
print(xmen_file.read())
xmen_file.seek(0)
for line in xmen_file:
    print(line, end="")
xmen_file.close()

# Creating a New File and Writing to It
xmen_base = open(xmen_base_txt)
new_xmen = open('new_xmen.txt', 'w')
new_xmen.write(xmen_base.read())
new_xmen.close()
new_xmen = open(new_xmen.name, 'r+')
print(new_xmen.read())
print(new_xmen.seek(0))
print(new_xmen.write("Beast\n"))
print(new_xmen.write("Phoenix\n"))
print(new_xmen.seek(0))
print(new_xmen.read())

# Appending to a File
xmen_file.close()
with open(xmen_base_txt, 'a') as f:
    f.write('Professor Xavier\n')

f = open(xmen_base_txt, 'a')
with f:
    f.write("Something\n")

exit()
