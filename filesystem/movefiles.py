import os

source = "text.txt"
destination = "C:\\Users\\scott\\OneDrive\\Desktop\\text.txt"

try:
    if os.path.exists(destination):
        print('File already exists')
    else:
        os.replace(source, destination)
        print(source + " was moved")

except FileNotFoundError:
    print(source + " was not found")

except Exception as e:
    print(e)