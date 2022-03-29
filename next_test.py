
# next(, Default)
print (next((i for i in range(10) if i**2 == 17), None))

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)


# Initialize list
Lst = [50, 70, 30, 20, 90, 10, 50]

# Display list
print(Lst[::])
print(Lst[3::])
