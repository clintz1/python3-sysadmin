zero = 0
one = 1

# The not Operation
name = ""
print(not name)
if not name:
    print("No name given")

# The or Operation
first = ""
last = "Thompson"
if first or last:
    print("The user has a first or last name")
first = ""
last = ""
if first or last:
    print("The user has a first or last name")
last = ""
last_name = last or "Doe"
print(last_name)
print(zero or 1)
print(one or 2)

# The and Operation
first = "Keith"
last = ""
if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last name: {last}")
print(zero and 1)
print(one and 2)
print((1 == one) and print("Something"))
print((1 == 2) and print("Something"))
