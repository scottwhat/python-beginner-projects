

#open auto closes after reading
with open('test.txt') as file:
    print(file.read())

#
print(file.closed)
print()

