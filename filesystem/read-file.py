

#open auto closes after reading
with open('text.txt') as file:
    print(file.read())

#
print(file.closed)
print()

