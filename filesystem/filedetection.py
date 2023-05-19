import os

path = "C:\\Users\\scott\\OneDrive\\Desktop\\pathtest.docx"

if os.path.exists(path):
    print('That path exists')
    if os.path.isfile(path):
        print('that is a file too!')
    elif os.path.isdir(path):
        print("thats a directory")

else:
    print("Location doesnt exist")